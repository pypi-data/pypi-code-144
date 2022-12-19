import os

from srcmlcpp.scrml_warning_settings import WarningType
from codemanip import amalgamated_header
from codemanip.code_utils import join_string_by_pipe_char

import litgen


_THIS_DIR = os.path.dirname(__file__)
LG_HELLO_IMGUI_DIR = os.path.realpath(_THIS_DIR + "/..")
CPP_HEADERS_DIR = LG_HELLO_IMGUI_DIR + "/external/hello_imgui/src/hello_imgui"
CPP_GENERATED_PYBIND_DIR = LG_HELLO_IMGUI_DIR + "/bindings"
assert os.path.isdir(CPP_HEADERS_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def make_hello_imgui_amalgamated_header():
    hello_imgui_src_dir = LG_HELLO_IMGUI_DIR + "/external/hello_imgui/src/"

    options = amalgamated_header.AmalgamationOptions()

    options.base_dir = hello_imgui_src_dir
    options.local_includes_startwith = "hello_imgui/"
    options.include_subdirs = ["hello_imgui"]
    options.main_header_file = "hello_imgui.h"
    options.dst_amalgamated_header_file = _THIS_DIR + "/hello_imgui_amalgamation.h"

    amalgamated_header.write_amalgamate_header_file(options)


def autogenerate_hello_imgui():
    print("autogenerate_hello_imgui")
    make_hello_imgui_amalgamated_header()

    input_cpp_header = _THIS_DIR + "/hello_imgui_amalgamation.h"
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_hello_imgui.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/imgui_bundle/hello_imgui.pyi"

    # Configure options
    from codemanip.code_replacements import RegexReplacement

    options = litgen.LitgenOptions()
    # options.original_location_flag_show = True
    options.original_signature_flag_show = True
    options.srcmlcpp_options.ignored_warnings = [WarningType.LitgenIgnoreElement]
    options.srcmlcpp_options.ignored_warning_parts = ["gAssetsSubfolderFolderName"]
    options.namespace_names_replacements.add_last_replacement("ImGui", "Imgui")
    options.namespace_root__regex = "^HelloImGui$|^ImGuiTheme$"
    options.fn_return_force_policy_reference_for_pointers__regex = join_string_by_pipe_char(
        [r"\bLoadFontTTF\w*", r"MergeFontAwesomeToLastFont"]
    )
    options.var_names_replacements.replacements = [
        RegexReplacement("imGui", "imgui"),
        RegexReplacement("ImGui", "Imgui"),
    ]
    options.function_names_replacements.replacements = [
        # RegexReplacement("imGui", "imgui"),
        RegexReplacement("ImGui", "Imgui"),
    ]
    options.fn_return_force_policy_reference_for_pointers__regex = r".*"
    # setAssetsFolder & SetAssetsFolder offer the same function
    options.fn_exclude_by_name__regex = r"^setAssetsFolder$"

    litgen.write_generated_code_for_file(
        options,
        input_cpp_header_file=input_cpp_header,
        output_cpp_pydef_file=output_cpp_pydef_file,
        output_stub_pyi_file=output_stub_pyi_file,
    )


if __name__ == "__main__":
    autogenerate_hello_imgui()
