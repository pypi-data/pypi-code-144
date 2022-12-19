# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:48:57 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
misc.update(
    {
        "DRFileForkSizeInfo": objc.createStructType(
            "DiscRecording.DRFileForkSizeInfo",
            b"{DRFileForkSizeInfo=IIQ}",
            ["fork", "query", "size"],
        ),
        "DRFileProductionInfo": objc.createStructType(
            "DiscRecording.DRFileProductionInfo",
            b"{DRFileProductionInfo=Q^vIIII}",
            ["requestedAddress", "buffer", "reqCount", "actCount", "blockSize", "fork"],
        ),
        "DRTrackProductionInfo": objc.createStructType(
            "DiscRecording.DRTrackProductionInfo",
            b"{DRTrackProductionInfo=^vIIIIQ}",
            [
                "buffer",
                "reqCount",
                "actCount",
                "flags",
                "blockSize",
                "requestedAddress",
            ],
        ),
    }
)
constants = """$DRAbstractFile$DRAccessDate$DRAllFilesystems$DRApplicationIdentifier$DRAttributeModificationDate$DRAudioFourChannelKey$DRAudioPreEmphasisKey$DRBackupDate$DRBibliographicFile$DRBlockSize$DRBlockSizeKey$DRBlockTypeKey$DRBurnAppendableKey$DRBurnCompletionActionEject$DRBurnCompletionActionKey$DRBurnCompletionActionMount$DRBurnDoubleLayerL0DataZoneBlocksKey$DRBurnFailureActionEject$DRBurnFailureActionKey$DRBurnFailureActionNone$DRBurnOverwriteDiscKey$DRBurnRequestedSpeedKey$DRBurnStatusChangedNotification$DRBurnStrategyBDDAO$DRBurnStrategyCDSAO$DRBurnStrategyCDTAO$DRBurnStrategyDVDDAO$DRBurnStrategyIsRequiredKey$DRBurnStrategyKey$DRBurnTestingKey$DRBurnUnderrunProtectionKey$DRBurnVerifyDiscKey$DRCDTextArrangerKey$DRCDTextCharacterCodeKey$DRCDTextClosedKey$DRCDTextComposerKey$DRCDTextCopyrightAssertedForNamesKey$DRCDTextCopyrightAssertedForSpecialMessagesKey$DRCDTextCopyrightAssertedForTitlesKey$DRCDTextDiscIdentKey$DRCDTextGenreCodeKey$DRCDTextGenreKey$DRCDTextKey$DRCDTextLanguageKey$DRCDTextMCNISRCKey$DRCDTextNSStringEncodingKey$DRCDTextPerformerKey$DRCDTextSizeKey$DRCDTextSongwriterKey$DRCDTextSpecialMessageKey$DRCDTextTOC2Key$DRCDTextTOCKey$DRCDTextTitleKey$DRContentModificationDate$DRCopyrightFile$DRCreationDate$DRDVDCopyrightInfoKey$DRDVDTimestampKey$DRDataFormKey$DRDataPreparer$DRDefaultDate$DRDeviceAppearedNotification$DRDeviceBurnSpeedBD1x@f$DRDeviceBurnSpeedCD1x@f$DRDeviceBurnSpeedDVD1x@f$DRDeviceBurnSpeedHDDVD1x@f$DRDeviceBurnSpeedMax@f$DRDeviceBurnSpeedsKey$DRDeviceCanTestWriteCDKey$DRDeviceCanTestWriteDVDKey$DRDeviceCanUnderrunProtectCDKey$DRDeviceCanUnderrunProtectDVDKey$DRDeviceCanWriteBDKey$DRDeviceCanWriteBDREKey$DRDeviceCanWriteBDRKey$DRDeviceCanWriteCDKey$DRDeviceCanWriteCDRKey$DRDeviceCanWriteCDRWKey$DRDeviceCanWriteCDRawKey$DRDeviceCanWriteCDSAOKey$DRDeviceCanWriteCDTAOKey$DRDeviceCanWriteCDTextKey$DRDeviceCanWriteDVDDAOKey$DRDeviceCanWriteDVDKey$DRDeviceCanWriteDVDPlusRDoubleLayerKey$DRDeviceCanWriteDVDPlusRKey$DRDeviceCanWriteDVDPlusRWDoubleLayerKey$DRDeviceCanWriteDVDPlusRWKey$DRDeviceCanWriteDVDRAMKey$DRDeviceCanWriteDVDRDualLayerKey$DRDeviceCanWriteDVDRKey$DRDeviceCanWriteDVDRWDualLayerKey$DRDeviceCanWriteDVDRWKey$DRDeviceCanWriteHDDVDKey$DRDeviceCanWriteHDDVDRAMKey$DRDeviceCanWriteHDDVDRDualLayerKey$DRDeviceCanWriteHDDVDRKey$DRDeviceCanWriteHDDVDRWDualLayerKey$DRDeviceCanWriteHDDVDRWKey$DRDeviceCanWriteISRCKey$DRDeviceCanWriteIndexPointsKey$DRDeviceCanWriteKey$DRDeviceCurrentWriteSpeedKey$DRDeviceDisappearedNotification$DRDeviceFirmwareRevisionKey$DRDeviceIORegistryEntryPathKey$DRDeviceIsBusyKey$DRDeviceIsTrayOpenKey$DRDeviceLoadingMechanismCanEjectKey$DRDeviceLoadingMechanismCanInjectKey$DRDeviceLoadingMechanismCanOpenKey$DRDeviceMaximumWriteSpeedKey$DRDeviceMediaBSDNameKey$DRDeviceMediaBlocksFreeKey$DRDeviceMediaBlocksOverwritableKey$DRDeviceMediaBlocksUsedKey$DRDeviceMediaClassBD$DRDeviceMediaClassCD$DRDeviceMediaClassDVD$DRDeviceMediaClassHDDVD$DRDeviceMediaClassKey$DRDeviceMediaClassUnknown$DRDeviceMediaDoubleLayerL0DataZoneBlocksKey$DRDeviceMediaFreeSpaceKey$DRDeviceMediaInfoKey$DRDeviceMediaIsAppendableKey$DRDeviceMediaIsBlankKey$DRDeviceMediaIsErasableKey$DRDeviceMediaIsOverwritableKey$DRDeviceMediaIsReservedKey$DRDeviceMediaOverwritableSpaceKey$DRDeviceMediaSessionCountKey$DRDeviceMediaStateInTransition$DRDeviceMediaStateKey$DRDeviceMediaStateMediaPresent$DRDeviceMediaStateNone$DRDeviceMediaTrackCountKey$DRDeviceMediaTypeBDR$DRDeviceMediaTypeBDRE$DRDeviceMediaTypeBDROM$DRDeviceMediaTypeCDR$DRDeviceMediaTypeCDROM$DRDeviceMediaTypeCDRW$DRDeviceMediaTypeDVDPlusR$DRDeviceMediaTypeDVDPlusRDoubleLayer$DRDeviceMediaTypeDVDPlusRW$DRDeviceMediaTypeDVDPlusRWDoubleLayer$DRDeviceMediaTypeDVDR$DRDeviceMediaTypeDVDRAM$DRDeviceMediaTypeDVDRDualLayer$DRDeviceMediaTypeDVDROM$DRDeviceMediaTypeDVDRW$DRDeviceMediaTypeDVDRWDualLayer$DRDeviceMediaTypeHDDVDR$DRDeviceMediaTypeHDDVDRAM$DRDeviceMediaTypeHDDVDRDualLayer$DRDeviceMediaTypeHDDVDROM$DRDeviceMediaTypeHDDVDRW$DRDeviceMediaTypeHDDVDRWDualLayer$DRDeviceMediaTypeKey$DRDeviceMediaTypeUnknown$DRDeviceMediaUsedSpaceKey$DRDevicePhysicalInterconnectATAPI$DRDevicePhysicalInterconnectFibreChannel$DRDevicePhysicalInterconnectFireWire$DRDevicePhysicalInterconnectKey$DRDevicePhysicalInterconnectLocationExternal$DRDevicePhysicalInterconnectLocationInternal$DRDevicePhysicalInterconnectLocationKey$DRDevicePhysicalInterconnectLocationUnknown$DRDevicePhysicalInterconnectSCSI$DRDevicePhysicalInterconnectUSB$DRDeviceProductNameKey$DRDeviceStatusChangedNotification$DRDeviceSupportLevelAppleShipping$DRDeviceSupportLevelAppleSupported$DRDeviceSupportLevelKey$DRDeviceSupportLevelNone$DRDeviceSupportLevelUnsupported$DRDeviceSupportLevelVendorSupported$DRDeviceTrackInfoKey$DRDeviceTrackRefsKey$DRDeviceVendorNameKey$DRDeviceWriteBufferSizeKey$DRDeviceWriteCapabilitiesKey$DREffectiveDate$DREraseStatusChangedNotification$DREraseTypeComplete$DREraseTypeKey$DREraseTypeQuick$DRErrorStatusAdditionalSenseStringKey$DRErrorStatusErrorInfoStringKey$DRErrorStatusErrorKey$DRErrorStatusErrorStringKey$DRErrorStatusKey$DRErrorStatusSenseCodeStringKey$DRErrorStatusSenseKey$DRExpirationDate$DRFreeBlocksKey$DRHFSPlus$DRHFSPlusCatalogNodeID$DRHFSPlusTextEncodingHint$DRISO9660$DRISO9660LevelOne$DRISO9660LevelTwo$DRISO9660VersionNumber$DRISOLevel$DRISOMacExtensions$DRISORockRidgeExtensions$DRIndexPointsKey$DRInvisible$DRJoliet$DRLinkTypeFinderAlias$DRLinkTypeHardLink$DRLinkTypeSymbolicLink$DRMacExtendedFinderFlags$DRMacFileCreator$DRMacFileType$DRMacFinderFlags$DRMacFinderHideExtension$DRMacIconLocation$DRMacScrollPosition$DRMacWindowBounds$DRMacWindowView$DRMaxBurnSpeedKey$DRMediaCatalogNumberKey$DRNextWritableAddressKey$DRPosixFileMode$DRPosixGID$DRPosixUID$DRPreGapIsRequiredKey$DRPreGapLengthKey$DRPublisher$DRRecordingDate$DRSCMSCopyrightFree$DRSCMSCopyrightProtectedCopy$DRSCMSCopyrightProtectedOriginal$DRSerialCopyManagementStateKey$DRSessionFormatKey$DRSessionNumberKey$DRStatusCurrentSessionKey$DRStatusCurrentSpeedKey$DRStatusCurrentTrackKey$DRStatusEraseTypeKey$DRStatusPercentCompleteKey$DRStatusProgressCurrentKPS$DRStatusProgressCurrentXFactor$DRStatusProgressInfoKey$DRStatusStateDone$DRStatusStateErasing$DRStatusStateFailed$DRStatusStateFinishing$DRStatusStateKey$DRStatusStateNone$DRStatusStatePreparing$DRStatusStateSessionClose$DRStatusStateSessionOpen$DRStatusStateTrackClose$DRStatusStateTrackOpen$DRStatusStateTrackWrite$DRStatusStateVerifying$DRStatusTotalSessionsKey$DRStatusTotalTracksKey$DRSubchannelDataFormKey$DRSubchannelDataFormNone$DRSubchannelDataFormPack$DRSubchannelDataFormRaw$DRSuppressMacSpecificFiles$DRSynchronousBehaviorKey$DRSystemIdentifier$DRTrackISRCKey$DRTrackIsEmptyKey$DRTrackLengthKey$DRTrackModeKey$DRTrackNumberKey$DRTrackPacketSizeKey$DRTrackPacketTypeFixed$DRTrackPacketTypeKey$DRTrackPacketTypeVariable$DRTrackStartAddressKey$DRTrackTypeClosed$DRTrackTypeIncomplete$DRTrackTypeInvisible$DRTrackTypeKey$DRTrackTypeReserved$DRUDF$DRUDFApplicationIdentifierSuffix$DRUDFExtendedFilePermissions$DRUDFInterchangeLevel$DRUDFMaxInterchangeLevel$DRUDFMaxVolumeSequenceNumber$DRUDFPrimaryVolumeDescriptorNumber$DRUDFRealTimeFile$DRUDFVersion102$DRUDFVersion150$DRUDFVolumeSequenceNumber$DRUDFVolumeSetIdentifier$DRUDFVolumeSetImplementationUse$DRUDFVolumeSetTimestamp$DRUDFWriteVersion$DRVerificationTypeChecksum$DRVerificationTypeKey$DRVerificationTypeNone$DRVerificationTypeProduceAgain$DRVerificationTypeReceiveData$DRVolumeCheckedDate$DRVolumeCreationDate$DRVolumeEffectiveDate$DRVolumeExpirationDate$DRVolumeModificationDate$DRVolumeSet$kDRAbstractFile$kDRAccessDate$kDRAllFilesystems$kDRApplicationIdentifier$kDRAttributeModificationDate$kDRAudioFourChannelKey$kDRAudioPreEmphasisKey$kDRBackupDate$kDRBibliographicFile$kDRBlockSize$kDRBlockSizeKey$kDRBlockTypeKey$kDRBufferZone1DataKey$kDRBurnAppendableKey$kDRBurnCompletionActionEject$kDRBurnCompletionActionKey$kDRBurnCompletionActionMount$kDRBurnDoubleLayerL0DataZoneBlocksKey$kDRBurnFailureActionEject$kDRBurnFailureActionKey$kDRBurnFailureActionNone$kDRBurnKey$kDRBurnOverwriteDiscKey$kDRBurnRequestedSpeedKey$kDRBurnStatusChangedNotification$kDRBurnStrategyBDDAO$kDRBurnStrategyCDSAO$kDRBurnStrategyCDTAO$kDRBurnStrategyDVDDAO$kDRBurnStrategyIsRequiredKey$kDRBurnStrategyKey$kDRBurnTestingKey$kDRBurnUnderrunProtectionKey$kDRBurnVerifyDiscKey$kDRCDTextArrangerKey$kDRCDTextCFStringEncodingKey$kDRCDTextCharacterCodeKey$kDRCDTextClosedKey$kDRCDTextComposerKey$kDRCDTextCopyrightAssertedForNamesKey$kDRCDTextCopyrightAssertedForSpecialMessagesKey$kDRCDTextCopyrightAssertedForTitlesKey$kDRCDTextDiscIdentKey$kDRCDTextGenreCodeKey$kDRCDTextGenreKey$kDRCDTextKey$kDRCDTextLanguageKey$kDRCDTextMCNISRCKey$kDRCDTextPerformerKey$kDRCDTextSizeKey$kDRCDTextSongwriterKey$kDRCDTextSpecialMessageKey$kDRCDTextTOC2Key$kDRCDTextTOCKey$kDRCDTextTitleKey$kDRContentModificationDate$kDRCopyrightFile$kDRCreationDate$kDRDVDCopyrightInfoKey$kDRDVDTimestampKey$kDRDataFormKey$kDRDataPreparer$kDRDefaultDate$kDRDeviceAppearedNotification$kDRDeviceBurnSpeedBD1x@f$kDRDeviceBurnSpeedCD1x@f$kDRDeviceBurnSpeedDVD1x@f$kDRDeviceBurnSpeedHDDVD1x@f$kDRDeviceBurnSpeedMax@f$kDRDeviceBurnSpeedsKey$kDRDeviceCanTestWriteCDKey$kDRDeviceCanTestWriteDVDKey$kDRDeviceCanUnderrunProtectCDKey$kDRDeviceCanUnderrunProtectDVDKey$kDRDeviceCanWriteBDKey$kDRDeviceCanWriteBDREKey$kDRDeviceCanWriteBDRKey$kDRDeviceCanWriteCDKey$kDRDeviceCanWriteCDRKey$kDRDeviceCanWriteCDRWKey$kDRDeviceCanWriteCDRawKey$kDRDeviceCanWriteCDSAOKey$kDRDeviceCanWriteCDTAOKey$kDRDeviceCanWriteCDTextKey$kDRDeviceCanWriteDVDDAOKey$kDRDeviceCanWriteDVDKey$kDRDeviceCanWriteDVDPlusRDoubleLayerKey$kDRDeviceCanWriteDVDPlusRKey$kDRDeviceCanWriteDVDPlusRWDoubleLayerKey$kDRDeviceCanWriteDVDPlusRWKey$kDRDeviceCanWriteDVDRAMKey$kDRDeviceCanWriteDVDRDualLayerKey$kDRDeviceCanWriteDVDRKey$kDRDeviceCanWriteDVDRWDualLayerKey$kDRDeviceCanWriteDVDRWKey$kDRDeviceCanWriteHDDVDKey$kDRDeviceCanWriteHDDVDRAMKey$kDRDeviceCanWriteHDDVDRDualLayerKey$kDRDeviceCanWriteHDDVDRKey$kDRDeviceCanWriteHDDVDRWDualLayerKey$kDRDeviceCanWriteHDDVDRWKey$kDRDeviceCanWriteISRCKey$kDRDeviceCanWriteIndexPointsKey$kDRDeviceCanWriteKey$kDRDeviceCurrentWriteSpeedKey$kDRDeviceDisappearedNotification$kDRDeviceFirmwareRevisionKey$kDRDeviceIORegistryEntryPathKey$kDRDeviceIsBusyKey$kDRDeviceIsTrayOpenKey$kDRDeviceLoadingMechanismCanEjectKey$kDRDeviceLoadingMechanismCanInjectKey$kDRDeviceLoadingMechanismCanOpenKey$kDRDeviceMaximumWriteSpeedKey$kDRDeviceMediaBSDNameKey$kDRDeviceMediaBlocksFreeKey$kDRDeviceMediaBlocksOverwritableKey$kDRDeviceMediaBlocksUsedKey$kDRDeviceMediaClassBD$kDRDeviceMediaClassCD$kDRDeviceMediaClassDVD$kDRDeviceMediaClassHDDVD$kDRDeviceMediaClassKey$kDRDeviceMediaClassUnknown$kDRDeviceMediaDoubleLayerL0DataZoneBlocksKey$kDRDeviceMediaInfoKey$kDRDeviceMediaIsAppendableKey$kDRDeviceMediaIsBlankKey$kDRDeviceMediaIsErasableKey$kDRDeviceMediaIsOverwritableKey$kDRDeviceMediaIsReservedKey$kDRDeviceMediaSessionCountKey$kDRDeviceMediaStateInTransition$kDRDeviceMediaStateKey$kDRDeviceMediaStateMediaPresent$kDRDeviceMediaStateNone$kDRDeviceMediaTrackCountKey$kDRDeviceMediaTypeBDR$kDRDeviceMediaTypeBDRE$kDRDeviceMediaTypeBDROM$kDRDeviceMediaTypeCDR$kDRDeviceMediaTypeCDROM$kDRDeviceMediaTypeCDRW$kDRDeviceMediaTypeDVDPlusR$kDRDeviceMediaTypeDVDPlusRDoubleLayer$kDRDeviceMediaTypeDVDPlusRW$kDRDeviceMediaTypeDVDPlusRWDoubleLayer$kDRDeviceMediaTypeDVDR$kDRDeviceMediaTypeDVDRAM$kDRDeviceMediaTypeDVDRDualLayer$kDRDeviceMediaTypeDVDROM$kDRDeviceMediaTypeDVDRW$kDRDeviceMediaTypeDVDRWDualLayer$kDRDeviceMediaTypeHDDVDR$kDRDeviceMediaTypeHDDVDRAM$kDRDeviceMediaTypeHDDVDRDualLayer$kDRDeviceMediaTypeHDDVDROM$kDRDeviceMediaTypeHDDVDRW$kDRDeviceMediaTypeHDDVDRWDualLayer$kDRDeviceMediaTypeKey$kDRDeviceMediaTypeUnknown$kDRDevicePhysicalInterconnectATAPI$kDRDevicePhysicalInterconnectFibreChannel$kDRDevicePhysicalInterconnectFireWire$kDRDevicePhysicalInterconnectKey$kDRDevicePhysicalInterconnectLocationExternal$kDRDevicePhysicalInterconnectLocationInternal$kDRDevicePhysicalInterconnectLocationKey$kDRDevicePhysicalInterconnectLocationUnknown$kDRDevicePhysicalInterconnectSCSI$kDRDevicePhysicalInterconnectUSB$kDRDeviceProductNameKey$kDRDeviceStatusChangedNotification$kDRDeviceSupportLevelAppleShipping$kDRDeviceSupportLevelAppleSupported$kDRDeviceSupportLevelKey$kDRDeviceSupportLevelNone$kDRDeviceSupportLevelUnsupported$kDRDeviceSupportLevelVendorSupported$kDRDeviceTrackInfoKey$kDRDeviceTrackRefsKey$kDRDeviceVendorNameKey$kDRDeviceWriteBufferSizeKey$kDRDeviceWriteCapabilitiesKey$kDREffectiveDate$kDREraseStatusChangedNotification$kDREraseTypeComplete$kDREraseTypeKey$kDREraseTypeQuick$kDRErrorStatusAdditionalSenseStringKey$kDRErrorStatusErrorInfoStringKey$kDRErrorStatusErrorKey$kDRErrorStatusErrorStringKey$kDRErrorStatusKey$kDRErrorStatusSenseCodeStringKey$kDRErrorStatusSenseKey$kDRExpirationDate$kDRFreeBlocksKey$kDRHFSPlus$kDRHFSPlusCatalogNodeID$kDRHFSPlusTextEncodingHint$kDRISO9660$kDRISO9660LevelOne$kDRISO9660LevelTwo$kDRISO9660VersionNumber$kDRISOLevel$kDRISOMacExtensions$kDRISORockRidgeExtensions$kDRIndexPointsKey$kDRInvisible$kDRJoliet$kDRMacExtendedFinderFlags$kDRMacFileCreator$kDRMacFileType$kDRMacFinderFlags$kDRMacFinderHideExtension$kDRMacIconLocation$kDRMacScrollPosition$kDRMacWindowBounds$kDRMacWindowView$kDRMaxBurnSpeedKey$kDRMediaCatalogNumberKey$kDRNextWritableAddressKey$kDRPosixFileMode$kDRPosixGID$kDRPosixUID$kDRPreGapIsRequiredKey$kDRPreGapLengthKey$kDRPublisher$kDRRecordingDate$kDRSCMSCopyrightFree$kDRSCMSCopyrightProtectedCopy$kDRSCMSCopyrightProtectedOriginal$kDRSerialCopyManagementStateKey$kDRSessionFormatKey$kDRSessionNumberKey$kDRStatusCurrentSessionKey$kDRStatusCurrentSpeedKey$kDRStatusCurrentTrackKey$kDRStatusEraseTypeKey$kDRStatusPercentCompleteKey$kDRStatusProgressCurrentKPS$kDRStatusProgressCurrentXFactor$kDRStatusProgressInfoKey$kDRStatusStateDone$kDRStatusStateErasing$kDRStatusStateFailed$kDRStatusStateFinishing$kDRStatusStateKey$kDRStatusStateNone$kDRStatusStatePreparing$kDRStatusStateSessionClose$kDRStatusStateSessionOpen$kDRStatusStateTrackClose$kDRStatusStateTrackOpen$kDRStatusStateTrackWrite$kDRStatusStateVerifying$kDRStatusTotalSessionsKey$kDRStatusTotalTracksKey$kDRSubchannelDataFormKey$kDRSubchannelDataFormNone$kDRSubchannelDataFormPack$kDRSubchannelDataFormRaw$kDRSuppressMacSpecificFiles$kDRSynchronousBehaviorKey$kDRSystemIdentifier$kDRTrackISRCKey$kDRTrackIsEmptyKey$kDRTrackLengthKey$kDRTrackModeKey$kDRTrackNumberKey$kDRTrackPacketSizeKey$kDRTrackPacketTypeFixed$kDRTrackPacketTypeKey$kDRTrackPacketTypeVariable$kDRTrackStartAddressKey$kDRTrackTypeClosed$kDRTrackTypeIncomplete$kDRTrackTypeInvisible$kDRTrackTypeKey$kDRTrackTypeReserved$kDRUDF$kDRUDFApplicationIdentifierSuffix$kDRUDFExtendedFilePermissions$kDRUDFInterchangeLevel$kDRUDFMaxInterchangeLevel$kDRUDFMaxVolumeSequenceNumber$kDRUDFPrimaryVolumeDescriptorNumber$kDRUDFRealTimeFile$kDRUDFVersion102$kDRUDFVersion150$kDRUDFVolumeSequenceNumber$kDRUDFVolumeSetIdentifier$kDRUDFVolumeSetImplementationUse$kDRUDFVolumeSetTimestamp$kDRUDFWriteVersion$kDRVerificationTypeChecksum$kDRVerificationTypeKey$kDRVerificationTypeNone$kDRVerificationTypeProduceAgain$kDRVerificationTypeReceiveData$kDRVolumeCheckedDate$kDRVolumeCreationDate$kDRVolumeEffectiveDate$kDRVolumeExpirationDate$kDRVolumeModificationDate$kDRVolumeSet$"""
enums = """$DRCDTextEncodingASCII@1$DRCDTextEncodingISOLatin1Modified@5$DRCDTextGenreCodeAdultContemporary@2$DRCDTextGenreCodeAlternativeRock@3$DRCDTextGenreCodeChildrens@4$DRCDTextGenreCodeClassical@5$DRCDTextGenreCodeContemporaryChristian@6$DRCDTextGenreCodeCountry@7$DRCDTextGenreCodeDance@8$DRCDTextGenreCodeEasyListening@9$DRCDTextGenreCodeErotic@10$DRCDTextGenreCodeFolk@11$DRCDTextGenreCodeGospel@12$DRCDTextGenreCodeHipHop@13$DRCDTextGenreCodeJazz@14$DRCDTextGenreCodeLatin@15$DRCDTextGenreCodeMusical@16$DRCDTextGenreCodeNewAge@17$DRCDTextGenreCodeOpera@18$DRCDTextGenreCodeOperetta@19$DRCDTextGenreCodePop@20$DRCDTextGenreCodeRap@21$DRCDTextGenreCodeReggae@22$DRCDTextGenreCodeRhythmAndBlues@24$DRCDTextGenreCodeRock@23$DRCDTextGenreCodeSoundEffects@25$DRCDTextGenreCodeSoundtrack@26$DRCDTextGenreCodeSpokenWord@27$DRCDTextGenreCodeUnknown@1$DRCDTextGenreCodeWorldMusic@28$DRFileForkData@0$DRFileForkResource@1$DRFilesystemInclusionMaskHFSPlus@8$DRFilesystemInclusionMaskISO9660@1$DRFilesystemInclusionMaskJoliet@2$DRFilesystemInclusionMaskUDF@4$DRFlagSubchannelDataRequested@2$kDRAudioFileNotSupportedErr@2147614828$kDRBadLayoutErr@2147614821$kDRBlockSizeAudio@2352$kDRBlockSizeDVDData@2048$kDRBlockSizeMode1Data@2048$kDRBlockSizeMode2Data@2332$kDRBlockSizeMode2Form1Data@2048$kDRBlockSizeMode2Form2Data@2324$kDRBlockTypeAudio@0$kDRBlockTypeDVDData@8$kDRBlockTypeMode1Data@8$kDRBlockTypeMode2Data@13$kDRBlockTypeMode2Form1Data@10$kDRBlockTypeMode2Form2Data@12$kDRBurnMediaWriteFailureErr@2147614830$kDRBurnNotAllowedErr@2147614817$kDRBurnPowerCalibrationErr@2147614829$kDRBurnUnderrunErr@2147614816$kDRCDTextEncodingASCII@1536$kDRCDTextEncodingISOLatin1Modified@513$kDRCDTextGenreCodeAdultContemporary@2$kDRCDTextGenreCodeAlternativeRock@3$kDRCDTextGenreCodeChildrens@4$kDRCDTextGenreCodeClassical@5$kDRCDTextGenreCodeContemporaryChristian@6$kDRCDTextGenreCodeCountry@7$kDRCDTextGenreCodeDance@8$kDRCDTextGenreCodeEasyListening@9$kDRCDTextGenreCodeErotic@10$kDRCDTextGenreCodeFolk@11$kDRCDTextGenreCodeGospel@12$kDRCDTextGenreCodeHipHop@13$kDRCDTextGenreCodeJazz@14$kDRCDTextGenreCodeLatin@15$kDRCDTextGenreCodeMusical@16$kDRCDTextGenreCodeNewAge@17$kDRCDTextGenreCodeOpera@18$kDRCDTextGenreCodeOperetta@19$kDRCDTextGenreCodePop@20$kDRCDTextGenreCodeRap@21$kDRCDTextGenreCodeReggae@22$kDRCDTextGenreCodeRhythmAndBlues@24$kDRCDTextGenreCodeRock@23$kDRCDTextGenreCodeSoundEffects@25$kDRCDTextGenreCodeSoundtrack@26$kDRCDTextGenreCodeSpokenWord@27$kDRCDTextGenreCodeUnknown@1$kDRCDTextGenreCodeWorldMusic@28$kDRDataFormAudio@0$kDRDataFormDVDData@16$kDRDataFormMode1Data@16$kDRDataFormMode2Data@32$kDRDataFormMode2Form1Data@32$kDRDataFormMode2Form2Data@32$kDRDataProductionErr@2147614818$kDRDeviceAccessErr@2147614752$kDRDeviceBurnStrategyNotAvailableErr@2147615232$kDRDeviceBusyErr@2147614753$kDRDeviceCantWriteCDTextErr@2147615233$kDRDeviceCantWriteISRCErr@2147615235$kDRDeviceCantWriteIndexPointsErr@2147615234$kDRDeviceCantWriteSCMSErr@2147615236$kDRDeviceCommunicationErr@2147614754$kDRDeviceInvalidErr@2147614755$kDRDeviceNotReadyErr@2147614756$kDRDeviceNotSupportedErr@2147614757$kDRDevicePreGapLengthNotValidErr@2147615237$kDRDoubleLayerL0AlreadySpecifiedErr@2147614827$kDRDoubleLayerL0DataZoneBlocksParamErr@2147614826$kDRFileForkData@0$kDRFileForkResource@1$kDRFileForkSizeActual@0$kDRFileForkSizeEstimate@1$kDRFileLocationConflictErr@2147614977$kDRFileMessageForkSize@1718839674$kDRFileMessagePostBurn@1886352244$kDRFileMessagePreBurn@1886545184$kDRFileMessageProduceData@1886547812$kDRFileMessageRelease@1652122912$kDRFileMessageVerificationStarting@1987208825$kDRFileModifiedDuringBurnErr@2147614976$kDRFilesystemMaskDefault@4294967295$kDRFilesystemMaskHFSPlus@8$kDRFilesystemMaskISO9660@1$kDRFilesystemMaskJoliet@2$kDRFilesystemMaskUDF@4$kDRFilesystemsNotSupportedErr@2147614979$kDRFirstErr@2147614720$kDRFlagNoMoreData@1$kDRFlagSubchannelDataRequested@2$kDRFunctionNotSupportedErr@2147614823$kDRInternalErr@2147614720$kDRInvalidIndexPointsErr@2147614825$kDRLinkTypeFinderAlias@3$kDRLinkTypeHardLink@1$kDRLinkTypeSymbolicLink@2$kDRMediaBusyErr@2147614784$kDRMediaInvalidErr@2147614790$kDRMediaNotBlankErr@2147614788$kDRMediaNotErasableErr@2147614789$kDRMediaNotPresentErr@2147614785$kDRMediaNotSupportedErr@2147614787$kDRMediaNotWritableErr@2147614786$kDRSessionFormatAudio@0$kDRSessionFormatCDI@16$kDRSessionFormatCDXA@32$kDRSessionFormatDVDData@0$kDRSessionFormatMode1Data@0$kDRSpeedTestAlreadyRunningErr@2147614824$kDRTooManyNameConflictsErr@2147614978$kDRTooManyTracksForDVDErr@2147614820$kDRTrackMessageEstimateLength@1702065257$kDRTrackMessagePostBurn@1886352244$kDRTrackMessagePreBurn@1886545184$kDRTrackMessageProduceData@1886547812$kDRTrackMessageProducePreGap@1886548082$kDRTrackMessageVerificationDone@1986293614$kDRTrackMessageVerificationStarting@1987277938$kDRTrackMessageVerifyData@1987208825$kDRTrackMessageVerifyPreGap@1987211378$kDRTrackMode1Data@4$kDRTrackMode2Data@4$kDRTrackMode2Form1Data@4$kDRTrackMode2Form2Data@4$kDRTrackModeAudio@0$kDRTrackModeDVDData@5$kDRTrackReusedErr@2147614831$kDRUserCanceledErr@2147614822$kDRVerificationFailedErr@2147614819$"""
misc.update({})
misc.update({})
functions = {
    "DREraseCreate": (
        b"^{__DRErase=}^{__DRDevice=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRDeviceCopyStatus": (
        b"^{__CFDictionary=}^{__DRDevice=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFilesystemTrackCreate": (
        b"^{__DRTrack=}^{__DRFolder=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRNotificationCenterCreateRunLoopSource": (
        b"^{__CFRunLoopSource=}^{__DRNotificationCenter=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockGetValue": (b"@^{__DRCDTextBlock=}q^{__CFString=}",),
    "DRDeviceAcquireExclusiveAccess": (b"i^{__DRDevice=}",),
    "DRNotificationCenterCreate": (
        b"^{__DRNotificationCenter=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRBurnGetDevice": (b"^{__DRDevice=}^{__DRBurn=}",),
    "DREraseCopyStatus": (
        b"^{__CFDictionary=}^{__DRErase=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFilesystemTrackEstimateOverhead": (b"QQII",),
    "DRFSObjectSetBaseName": (b"v@^{__CFString=}",),
    "DRDeviceGetTypeID": (b"Q",),
    "DRBurnGetProperties": (b"^{__CFDictionary=}^{__DRBurn=}",),
    "DREraseGetDevice": (b"^{__DRDevice=}^{__DRErase=}",),
    "DRCopyLocalizedStringForAdditionalSense": (
        b"^{__CFString=}CC",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFSObjectIsVirtual": (b"Z@",),
    "DRNotificationCenterAddObserver": (
        b"v^{__DRNotificationCenter=}^v^?^{__CFString=}@",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DRNotificationCenter=}"},
                            1: {"type": b"^v"},
                            2: {"type": b"^{__CFString=}"},
                            3: {"type": b"@"},
                            4: {"type": b"^{__CFDictionary=}"},
                        },
                    }
                }
            }
        },
    ),
    "DRFolderCopyChildren": (
        b"^{__CFArray=}^{__DRFolder=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRDeviceIsValid": (b"Z^{__DRDevice=}",),
    "DRCopyLocalizedStringForValue": (
        b"^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRNotificationCenterRemoveObserver": (
        b"v^{__DRNotificationCenter=}^v^{__CFString=}@",
    ),
    "DRBurnSetProperties": (b"v^{__DRBurn=}^{__CFDictionary=}",),
    "DRBurnGetTypeID": (b"Q",),
    "DRFSObjectSetSpecificName": (b"v@^{__CFString=}^{__CFString=}",),
    "DRFolderCreateReal": (
        b"^{__DRFolder=}^{FSRef=[80C]}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "n"}},
        },
    ),
    "DRTrackSpeedTest": (b"f^{__DRTrack=}II",),
    "DRCDTextBlockCreateArrayFromPackList": (
        b"^{__CFArray=}^{__CFData=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockSetTrackDictionaries": (b"v^{__DRCDTextBlock=}^{__CFArray=}",),
    "DRDeviceReleaseMediaReservation": (b"v^{__DRDevice=}",),
    "DRCDTextBlockGetProperties": (b"^{__CFDictionary=}^{__DRCDTextBlock=}",),
    "DRDeviceCloseTray": (b"i^{__DRDevice=}",),
    "DRBurnCopyStatus": (
        b"^{__CFDictionary=}^{__DRBurn=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRDeviceKPSForXFactor": (b"f@f",),
    "DRFSObjectGetFilesystemMask": (
        b"I@^I^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "DRFolderCreateVirtual": (
        b"^{__DRFolder=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DREraseGetTypeID": (b"Q",),
    "DRDeviceOpenTray": (b"i^{__DRDevice=}",),
    "DRFSObjectSetFilesystemProperties": (b"v@^{__CFString=}^{__CFDictionary=}",),
    "DRFSObjectCopyBaseName": (
        b"^{__CFString=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFileCreateRealWithURL": (
        b"^{__DRFile=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRDeviceXFactorForKPS": (b"f@f",),
    "DRFSObjectCopySpecificNames": (
        b"^{__CFDictionary=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFolderConvertRealToVirtual": (b"v^{__DRFolder=}",),
    "DRCopyDeviceArray": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockGetTrackDictionaries": (b"^{__CFArray=}^{__DRCDTextBlock=}",),
    "DRFSObjectSetFilesystemProperty": (b"v@^{__CFString=}^{__CFString=}@",),
    "DRFileCreateVirtualWithData": (
        b"^{__DRFile=}^{__CFString=}^vI",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"c_array_length_in_arg": 2, "type_modifier": "n"}},
        },
    ),
    "DREraseGetProperties": (b"^{__CFDictionary=}^{__DRErase=}",),
    "DRDeviceCopyDeviceForIORegistryEntryPath": (
        b"^{__DRDevice=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFSObjectCopyFilesystemProperty": (
        b"@@^{__CFString=}^{__CFString=}Z",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFileCreateReal": (
        b"^{__DRFile=}^{FSRef=[80C]}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "n"}},
        },
    ),
    "DRCopyLocalizedStringForSenseCode": (
        b"^{__CFString=}C",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockFlatten": (b"I^{__DRCDTextBlock=}",),
    "DRSetRefCon": (b"v@^v^{DRRefConCallbacks=Q^?^?}",),
    "DRFSObjectCopyRealURL": (
        b"^{__CFURL=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFileCreateVirtualLink": (
        b"^{__DRFile=}@I^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFSObjectGetRealFSRef": (
        b"v@^{FSRef=[80C]}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "DRDeviceEjectMedia": (b"i^{__DRDevice=}",),
    "DRAudioTrackCreateWithURL": (
        b"^{__DRTrack=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCopyLocalizedStringForDiscRecordingError": (
        b"^{__CFString=}i",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFSObjectCopyFilesystemProperties": (
        b"^{__CFDictionary=}@^{__CFString=}Z",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRTrackGetProperties": (b"^{__CFDictionary=}^{__DRTrack=}",),
    "DRFolderAddChild": (b"v^{__DRFolder=}@",),
    "DRNotificationCenterGetTypeID": (b"Q",),
    "DRFolderCountChildren": (b"I^{__DRFolder=}",),
    "DRFileCreateVirtualWithCallback": (
        b"^{__DRFile=}^{__CFString=}^?^v",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{__DRFile=}"},
                            2: {"type": b"I"},
                            3: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "DRBurnCreate": (
        b"^{__DRBurn=}^{__DRDevice=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRDeviceReleaseExclusiveAccess": (b"v^{__DRDevice=}",),
    "DRGetRefCon": (b"^v@",),
    "DRGetVersion": (b"{NumVersion=CCCC}",),
    "DRFSObjectSetSpecificNames": (b"v@^{__CFDictionary=}",),
    "DRDeviceAcquireMediaReservation": (b"v^{__DRDevice=}",),
    "DRTrackSetProperties": (b"v^{__DRTrack=}^{__CFDictionary=}",),
    "DRFSObjectCopySpecificName": (
        b"^{__CFString=}@^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockSetValue": (b"v^{__DRCDTextBlock=}q^{__CFString=}@",),
    "DREraseSetProperties": (b"v^{__DRErase=}^{__CFDictionary=}",),
    "DREraseStart": (b"i^{__DRErase=}",),
    "DRFolderRemoveChild": (b"v^{__DRFolder=}@",),
    "DRFolderGetTypeID": (b"Q",),
    "DRBurnWriteLayout": (b"i^{__DRBurn=}@",),
    "DRTrackEstimateLength": (b"Q^{__DRTrack=}",),
    "DRBurnAbort": (b"v^{__DRBurn=}",),
    "DRFSObjectGetParent": (b"^{__DRFolder=}@",),
    "DRFSObjectSetFilesystemMask": (b"v@I",),
    "DRFileGetTypeID": (b"Q",),
    "DRCDTextBlockSetProperties": (b"v^{__DRCDTextBlock=}^{__CFDictionary=}",),
    "DRDeviceCopyDeviceForBSDName": (
        b"^{__DRDevice=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFSObjectCopyMangledNames": (
        b"^{__CFDictionary=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockGetTypeID": (b"Q",),
    "DRAudioTrackCreate": (
        b"^{__DRTrack=}^{FSRef=[80C]}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "n"}},
        },
    ),
    "DRTrackCreate": (
        b"^{__DRTrack=}^{__CFDictionary=}^?",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": b"^{__DRTrack=}"},
                            1: {"type": b"I"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "DRFolderCreateRealWithURL": (
        b"^{__DRFolder=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRCDTextBlockCreate": (
        b"^{__DRCDTextBlock=}^{__CFString=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRFSObjectCopyMangledName": (
        b"^{__CFString=}@^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRDeviceCopyInfo": (
        b"^{__CFDictionary=}^{__DRDevice=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DRTrackGetTypeID": (b"Q",),
}
aliases = {
    "DRAudioTrackRef": "DRTrackRef",
    "DRCDTextEncodingASCII": "NSASCIIStringEncoding",
    "kDRCDTextEncodingASCII": "kCFStringEncodingASCII",
    "DRCDTextEncodingISOLatin1Modified": "NSISOLatin1StringEncoding",
    "kDRInternalErr": "kDRFirstErr",
    "kDRCDTextEncodingISOLatin1Modified": "kCFStringEncodingISOLatin1",
    "DRFilesystemTrackRef": "DRTrackRef",
}
cftypes = [
    ("DRBurnRef", b"^{__DRBurn=}", None, None),
    ("DRCDTextBlockRef", b"^{__DRCDTextBlock=}", None, None),
    ("DRDeviceRef", b"^{__DRDevice=}", None, None),
    ("DREraseRef", b"^{__DRErase=}", None, None),
    ("DRFileRef", b"^{__DRFile=}", None, None),
    ("DRFolderRef", b"^{__DRFolder=}", None, None),
    ("DRNotificationCenterRef", b"^{__DRNotificationCenter=}", None, None),
    ("DRTrackRef", b"^{__DRTrack=}", None, None),
]
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"DRBurn", b"appendable", {"retval": {"type": b"Z"}})
    r(b"DRBurn", b"setAppendable:", {"arguments": {2: {"type": b"Z"}}})
    r(b"DRBurn", b"setVerifyDisc:", {"arguments": {2: {"type": b"Z"}}})
    r(b"DRBurn", b"verifyDisc", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"acquireExclusiveAccess", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"closeTray", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"ejectMedia", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"isEqualToDevice:", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"isValid", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsAppendable", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsBlank", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsBusy", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsErasable", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsOverwritable", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsPresent", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsReserved", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"mediaIsTransitioning", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"openTray", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"trayIsOpen", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"writesCD", {"retval": {"type": b"Z"}})
    r(b"DRDevice", b"writesDVD", {"retval": {"type": b"Z"}})
    r(b"DRFSObject", b"isVirtual", {"retval": {"type": b"Z"}})
    r(
        b"DRFSObject",
        b"propertiesForFilesystem:mergeWithOtherFilesystems:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"DRFSObject",
        b"propertyForKey:inFilesystem:mergeWithOtherFilesystems:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"DRMSF", b"isEqualToMSF:", {"retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"calculateSizeOfFile:fork:estimating:",
        {
            "required": True,
            "retval": {"type": b"Q"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"I"}, 4: {"type": b"Z"}},
        },
    )
    r(
        b"NSObject",
        b"cleanupFileAfterBurn:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"cleanupTrackAfterBurn:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"cleanupTrackAfterVerification:",
        {"required": True, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"estimateLengthOfTrack:",
        {"required": True, "retval": {"type": b"Q"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"prepareFileForBurn:",
        {"required": True, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"prepareFileForVerification:",
        {"required": True, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"prepareTrack:forBurn:toMedia:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"prepareTrackForVerification:",
        {"required": True, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"produceDataForTrack:intoBuffer:length:atAddress:blockSize:ioFlags:",
        {
            "required": True,
            "retval": {"type": b"I"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^v", "type_modifier": b"o", "c_array_length_in_arg": 4},
                4: {"type": b"I"},
                5: {"type": b"Q"},
                6: {"type": b"I"},
                7: {"type": b"^I", "type_modifier": b"N"},
            },
        },
    )
    r(
        b"NSObject",
        b"produceFile:fork:intoBuffer:length:atAddress:blockSize:",
        {
            "required": True,
            "retval": {"type": b"I"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"I"},
                4: {"type": "^v", "type_modifier": b"o", "c_array_length_in_arg": 5},
                5: {"type": b"I"},
                6: {"type": b"Q"},
                7: {"type": b"I"},
            },
        },
    )
    r(
        b"NSObject",
        b"producePreGapForTrack:intoBuffer:length:atAddress:blockSize:ioFlags:",
        {
            "required": True,
            "retval": {"type": b"I"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^v", "type_modifier": b"o", "c_array_length_in_arg": 4},
                4: {"type": b"I"},
                5: {"type": b"Q"},
                6: {"type": b"I"},
                7: {"type": b"^I", "type_modifier": b"N"},
            },
        },
    )
    r(
        b"NSObject",
        b"verifyDataForTrack:inBuffer:length:atAddress:blockSize:ioFlags:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^v", "type_modifier": b"n", "c_array_length_in_arg": 4},
                4: {"type": b"I"},
                5: {"type": b"Q"},
                6: {"type": b"I"},
                7: {"type": b"^I", "type_modifier": b"N"},
            },
        },
    )
    r(
        b"NSObject",
        b"verifyPreGapForTrack:inBuffer:length:atAddress:blockSize:ioFlags:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^v", "type_modifier": b"n", "c_array_length_in_arg": 4},
                4: {"type": b"I"},
                5: {"type": b"Q"},
                6: {"type": b"I"},
                7: {"type": b"^I", "type_modifier": b"N"},
            },
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
