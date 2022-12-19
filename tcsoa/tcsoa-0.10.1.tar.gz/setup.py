# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tcsoa',
 'tcsoa.fcc',
 'tcsoa.gen',
 'tcsoa.gen.AWS2',
 'tcsoa.gen.AWS2._2016_12',
 'tcsoa.gen.AWS2._2017_06',
 'tcsoa.gen.AWS2._2018_12',
 'tcsoa.gen.ActiveCollaboration',
 'tcsoa.gen.ActiveCollaboration._2020_12',
 'tcsoa.gen.ActiveWorkspaceBom',
 'tcsoa.gen.ActiveWorkspaceBom._2015_10',
 'tcsoa.gen.ActiveWorkspaceVis',
 'tcsoa.gen.ActiveWorkspaceVis._2015_03',
 'tcsoa.gen.Administration',
 'tcsoa.gen.Administration._2006_03',
 'tcsoa.gen.Administration._2007_01',
 'tcsoa.gen.Administration._2007_06',
 'tcsoa.gen.Administration._2008_03',
 'tcsoa.gen.Administration._2008_06',
 'tcsoa.gen.Administration._2008_12',
 'tcsoa.gen.Administration._2010_04',
 'tcsoa.gen.Administration._2011_05',
 'tcsoa.gen.Administration._2012_09',
 'tcsoa.gen.Administration._2012_10',
 'tcsoa.gen.Administration._2014_10',
 'tcsoa.gen.Administration._2015_03',
 'tcsoa.gen.Administration._2015_07',
 'tcsoa.gen.Administration._2016_03',
 'tcsoa.gen.Administration._2016_10',
 'tcsoa.gen.Administration._2017_05',
 'tcsoa.gen.Administration._2018_11',
 'tcsoa.gen.Ai',
 'tcsoa.gen.Ai._2006_03',
 'tcsoa.gen.Ai._2007_12',
 'tcsoa.gen.Ai._2008_05',
 'tcsoa.gen.Ai._2008_06',
 'tcsoa.gen.Ai._2009_06',
 'tcsoa.gen.Ai._2009_10',
 'tcsoa.gen.Ai._2010_09',
 'tcsoa.gen.Ai._2012_09',
 'tcsoa.gen.Ai._2013_05',
 'tcsoa.gen.Ai._2013_12',
 'tcsoa.gen.Ai._2014_12',
 'tcsoa.gen.Ai._2018_06',
 'tcsoa.gen.Allocations',
 'tcsoa.gen.Allocations._2007_01',
 'tcsoa.gen.Allocations._2011_06',
 'tcsoa.gen.AuthorizedDataAccess',
 'tcsoa.gen.AuthorizedDataAccess._2007_06',
 'tcsoa.gen.AuthorizedDataAccess._2009_10',
 'tcsoa.gen.AuthorizedDataAccess._2012_09',
 'tcsoa.gen.AuthorizedDataAccess._2013_05',
 'tcsoa.gen.AuthorizedDataAccess._2017_05',
 'tcsoa.gen.AuthorizedDataAccess._2018_06',
 'tcsoa.gen.Bom',
 'tcsoa.gen.Bom._2008_06',
 'tcsoa.gen.Bom._2010_09',
 'tcsoa.gen.BusinessModeler',
 'tcsoa.gen.BusinessModeler._2007_06',
 'tcsoa.gen.BusinessModeler._2008_06',
 'tcsoa.gen.BusinessModeler._2010_04',
 'tcsoa.gen.BusinessModeler._2011_06',
 'tcsoa.gen.Cad',
 'tcsoa.gen.Cad._2007_01',
 'tcsoa.gen.Cad._2007_06',
 'tcsoa.gen.Cad._2007_09',
 'tcsoa.gen.Cad._2007_12',
 'tcsoa.gen.Cad._2008_03',
 'tcsoa.gen.Cad._2008_06',
 'tcsoa.gen.Cad._2009_04',
 'tcsoa.gen.Cad._2010_09',
 'tcsoa.gen.Cad._2011_06',
 'tcsoa.gen.Cad._2012_09',
 'tcsoa.gen.Cad._2013_05',
 'tcsoa.gen.Cad._2014_10',
 'tcsoa.gen.Cad._2016_03',
 'tcsoa.gen.Cad._2016_09',
 'tcsoa.gen.Cad._2018_06',
 'tcsoa.gen.Cad._2019_06',
 'tcsoa.gen.Cad._2020_01',
 'tcsoa.gen.Cae',
 'tcsoa.gen.Cae._2009_10',
 'tcsoa.gen.Cae._2011_06',
 'tcsoa.gen.Cae._2012_02',
 'tcsoa.gen.Cae._2013_12',
 'tcsoa.gen.Cae._2014_06',
 'tcsoa.gen.CalendarManagement',
 'tcsoa.gen.CalendarManagement._2007_01',
 'tcsoa.gen.CalendarManagement._2007_06',
 'tcsoa.gen.CalendarManagement._2008_06',
 'tcsoa.gen.ChangeManagement',
 'tcsoa.gen.ChangeManagement._2008_06',
 'tcsoa.gen.ChangeManagement._2009_06',
 'tcsoa.gen.ChangeManagement._2015_10',
 'tcsoa.gen.ChangeManagement._2020_01',
 'tcsoa.gen.Classification',
 'tcsoa.gen.Classification._2007_01',
 'tcsoa.gen.Classification._2009_10',
 'tcsoa.gen.Classification._2011_06',
 'tcsoa.gen.Classification._2011_12',
 'tcsoa.gen.Classification._2015_03',
 'tcsoa.gen.Classification._2015_10',
 'tcsoa.gen.Classification._2016_03',
 'tcsoa.gen.Classification._2016_09',
 'tcsoa.gen.ClassificationCommon',
 'tcsoa.gen.ClassificationCommon._2020_01',
 'tcsoa.gen.ClassificationCommon._2020_12',
 'tcsoa.gen.ConfigFilterCriteria',
 'tcsoa.gen.ConfigFilterCriteria._2011_06',
 'tcsoa.gen.ConfigFilterCriteria._2013_05',
 'tcsoa.gen.ConfigFilterCriteria._2017_05',
 'tcsoa.gen.Configuration',
 'tcsoa.gen.Configuration._2010_04',
 'tcsoa.gen.Configurator',
 'tcsoa.gen.Configurator._2014_12',
 'tcsoa.gen.Core',
 'tcsoa.gen.Core._2006_03',
 'tcsoa.gen.Core._2007_01',
 'tcsoa.gen.Core._2007_06',
 'tcsoa.gen.Core._2007_09',
 'tcsoa.gen.Core._2007_12',
 'tcsoa.gen.Core._2008_03',
 'tcsoa.gen.Core._2008_05',
 'tcsoa.gen.Core._2008_06',
 'tcsoa.gen.Core._2009_04',
 'tcsoa.gen.Core._2009_10',
 'tcsoa.gen.Core._2010_04',
 'tcsoa.gen.Core._2010_09',
 'tcsoa.gen.Core._2011_06',
 'tcsoa.gen.Core._2012_02',
 'tcsoa.gen.Core._2012_09',
 'tcsoa.gen.Core._2012_10',
 'tcsoa.gen.Core._2013_05',
 'tcsoa.gen.Core._2014_06',
 'tcsoa.gen.Core._2014_10',
 'tcsoa.gen.Core._2015_07',
 'tcsoa.gen.Core._2015_10',
 'tcsoa.gen.Core._2016_05',
 'tcsoa.gen.Core._2016_09',
 'tcsoa.gen.Core._2016_10',
 'tcsoa.gen.Core._2017_05',
 'tcsoa.gen.Core._2017_11',
 'tcsoa.gen.Core._2018_06',
 'tcsoa.gen.Core._2018_11',
 'tcsoa.gen.Core._2019_06',
 'tcsoa.gen.Core._2020_01',
 'tcsoa.gen.Core._2020_04',
 'tcsoa.gen.Diagramming',
 'tcsoa.gen.Diagramming._2011_06',
 'tcsoa.gen.Diagramming._2012_09',
 'tcsoa.gen.Diagramming._2014_06',
 'tcsoa.gen.DocMgmtAw',
 'tcsoa.gen.DocMgmtAw._2017_06',
 'tcsoa.gen.DocumentManagement',
 'tcsoa.gen.DocumentManagement._2007_01',
 'tcsoa.gen.DocumentManagement._2008_06',
 'tcsoa.gen.DocumentManagement._2010_04',
 'tcsoa.gen.DocumentManagement._2011_06',
 'tcsoa.gen.DocumentManagement._2013_12',
 'tcsoa.gen.DocumentManagement._2018_06',
 'tcsoa.gen.DocumentManagement._2018_11',
 'tcsoa.gen.EditContext',
 'tcsoa.gen.EditContext._2014_12',
 'tcsoa.gen.EditContext._2015_07',
 'tcsoa.gen.EditContext._2016_04',
 'tcsoa.gen.EditContext._2016_10',
 'tcsoa.gen.GlobalMultiSite',
 'tcsoa.gen.GlobalMultiSite._2007_06',
 'tcsoa.gen.GlobalMultiSite._2007_12',
 'tcsoa.gen.GlobalMultiSite._2008_06',
 'tcsoa.gen.GlobalMultiSite._2010_04',
 'tcsoa.gen.GlobalMultiSite._2011_06',
 'tcsoa.gen.GlobalMultiSite._2020_04',
 'tcsoa.gen.ImportExport',
 'tcsoa.gen.ImportExport._2007_06',
 'tcsoa.gen.ImportExport._2008_06',
 'tcsoa.gen.ImportExport._2011_06',
 'tcsoa.gen.ImportExport._2012_09',
 'tcsoa.gen.ImportExport._2017_11',
 'tcsoa.gen.Internal',
 'tcsoa.gen.Internal.AWS2',
 'tcsoa.gen.Internal.AWS2._2012_10',
 'tcsoa.gen.Internal.AWS2._2013_12',
 'tcsoa.gen.Internal.AWS2._2014_11',
 'tcsoa.gen.Internal.AWS2._2015_03',
 'tcsoa.gen.Internal.AWS2._2015_10',
 'tcsoa.gen.Internal.AWS2._2016_03',
 'tcsoa.gen.Internal.AWS2._2016_04',
 'tcsoa.gen.Internal.AWS2._2016_12',
 'tcsoa.gen.Internal.AWS2._2017_06',
 'tcsoa.gen.Internal.AWS2._2017_12',
 'tcsoa.gen.Internal.AWS2._2018_05',
 'tcsoa.gen.Internal.AWS2._2018_12',
 'tcsoa.gen.Internal.AWS2._2019_06',
 'tcsoa.gen.Internal.AWS2._2019_12',
 'tcsoa.gen.Internal.AWS2._2020_05',
 'tcsoa.gen.Internal.AWS2._2020_12',
 'tcsoa.gen.Internal.ActiveWorkspaceBom',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2012_10',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2015_03',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2015_07',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2015_10',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2016_03',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2017_06',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2017_12',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2018_05',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2018_12',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2019_06',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2019_12',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2020_05',
 'tcsoa.gen.Internal.ActiveWorkspaceBom._2020_12',
 'tcsoa.gen.Internal.ActiveWorkspaceVis',
 'tcsoa.gen.Internal.ActiveWorkspaceVis._2014_11',
 'tcsoa.gen.Internal.ActiveWorkspaceVis._2015_03',
 'tcsoa.gen.Internal.ActiveWorkspaceVis._2018_05',
 'tcsoa.gen.Internal.Administration',
 'tcsoa.gen.Internal.Administration._2007_06',
 'tcsoa.gen.Internal.Administration._2008_06',
 'tcsoa.gen.Internal.Administration._2009_10',
 'tcsoa.gen.Internal.Administration._2011_06',
 'tcsoa.gen.Internal.Administration._2012_10',
 'tcsoa.gen.Internal.Administration._2013_05',
 'tcsoa.gen.Internal.Administration._2014_10',
 'tcsoa.gen.Internal.Administration._2016_09',
 'tcsoa.gen.Internal.Administration._2017_11',
 'tcsoa.gen.Internal.Administration._2018_11',
 'tcsoa.gen.Internal.Administration._2019_06',
 'tcsoa.gen.Internal.Ai',
 'tcsoa.gen.Internal.Ai._2008_06',
 'tcsoa.gen.Internal.Ai._2016_03',
 'tcsoa.gen.Internal.Ai._2016_04',
 'tcsoa.gen.Internal.AuditManager',
 'tcsoa.gen.Internal.AuditManager._2012_09',
 'tcsoa.gen.Internal.BusinessModeler',
 'tcsoa.gen.Internal.BusinessModeler._2007_01',
 'tcsoa.gen.Internal.BusinessModeler._2010_04',
 'tcsoa.gen.Internal.BusinessModeler._2010_09',
 'tcsoa.gen.Internal.BusinessModeler._2011_06',
 'tcsoa.gen.Internal.BusinessModeler._2013_05',
 'tcsoa.gen.Internal.Cad',
 'tcsoa.gen.Internal.Cad._2008_03',
 'tcsoa.gen.Internal.Cad._2008_05',
 'tcsoa.gen.Internal.Cad._2008_06',
 'tcsoa.gen.Internal.Cad._2010_04',
 'tcsoa.gen.Internal.Cad._2013_05',
 'tcsoa.gen.Internal.Cad._2017_05',
 'tcsoa.gen.Internal.Cae',
 'tcsoa.gen.Internal.Cae._2011_06',
 'tcsoa.gen.Internal.Cae._2013_05',
 'tcsoa.gen.Internal.Cae._2014_06',
 'tcsoa.gen.Internal.ChangeManagement',
 'tcsoa.gen.Internal.ChangeManagement._2012_10',
 'tcsoa.gen.Internal.ChangeManagement._2015_03',
 'tcsoa.gen.Internal.ChangeManagement._2020_01',
 'tcsoa.gen.Internal.Classification',
 'tcsoa.gen.Internal.Classification._2009_10',
 'tcsoa.gen.Internal.Classification._2017_05',
 'tcsoa.gen.Internal.Classification._2018_11',
 'tcsoa.gen.Internal.Classification._2020_04',
 'tcsoa.gen.Internal.ConfigFilterCriteria',
 'tcsoa.gen.Internal.ConfigFilterCriteria._2013_12',
 'tcsoa.gen.Internal.Configurator',
 'tcsoa.gen.Internal.Configurator._2014_06',
 'tcsoa.gen.Internal.Configurator._2014_12',
 'tcsoa.gen.Internal.Configurator._2015_03',
 'tcsoa.gen.Internal.Configurator._2015_10',
 'tcsoa.gen.Internal.Configurator._2016_09',
 'tcsoa.gen.Internal.Configurator._2017_11',
 'tcsoa.gen.Internal.Configurator._2018_06',
 'tcsoa.gen.Internal.Configurator._2018_11',
 'tcsoa.gen.Internal.Core',
 'tcsoa.gen.Internal.Core._2007_01',
 'tcsoa.gen.Internal.Core._2007_06',
 'tcsoa.gen.Internal.Core._2007_09',
 'tcsoa.gen.Internal.Core._2008_06',
 'tcsoa.gen.Internal.Core._2009_10',
 'tcsoa.gen.Internal.Core._2010_04',
 'tcsoa.gen.Internal.Core._2010_09',
 'tcsoa.gen.Internal.Core._2011_06',
 'tcsoa.gen.Internal.Core._2012_02',
 'tcsoa.gen.Internal.Core._2012_09',
 'tcsoa.gen.Internal.Core._2012_10',
 'tcsoa.gen.Internal.Core._2013_05',
 'tcsoa.gen.Internal.Core._2014_10',
 'tcsoa.gen.Internal.Core._2016_10',
 'tcsoa.gen.Internal.Core._2017_05',
 'tcsoa.gen.Internal.Core._2017_11',
 'tcsoa.gen.Internal.Core._2018_06',
 'tcsoa.gen.Internal.Core._2018_11',
 'tcsoa.gen.Internal.Core._2018_12',
 'tcsoa.gen.Internal.Core._2020_01',
 'tcsoa.gen.Internal.Core._2020_04',
 'tcsoa.gen.Internal.DebugMonitor',
 'tcsoa.gen.Internal.DebugMonitor._2011_06',
 'tcsoa.gen.Internal.DebugMonitor._2014_06',
 'tcsoa.gen.Internal.DebugMonitor._2015_07',
 'tcsoa.gen.Internal.DebugMonitor._2015_10',
 'tcsoa.gen.Internal.DebugMonitor._2019_06',
 'tcsoa.gen.Internal.DocMgmtAw',
 'tcsoa.gen.Internal.DocMgmtAw._2019_06',
 'tcsoa.gen.Internal.DocMgmtAw._2019_12',
 'tcsoa.gen.Internal.DocumentManagement',
 'tcsoa.gen.Internal.DocumentManagement._2008_06',
 'tcsoa.gen.Internal.DocumentManagement._2013_05',
 'tcsoa.gen.Internal.DocumentManagement._2013_12',
 'tcsoa.gen.Internal.DocumentManagement._2020_12',
 'tcsoa.gen.Internal.EntCba',
 'tcsoa.gen.Internal.EntCba._2019_12',
 'tcsoa.gen.Internal.Gdis',
 'tcsoa.gen.Internal.Gdis._2006_03',
 'tcsoa.gen.Internal.GlobalMultiSite',
 'tcsoa.gen.Internal.GlobalMultiSite._2007_06',
 'tcsoa.gen.Internal.GlobalMultiSite._2008_06',
 'tcsoa.gen.Internal.GlobalMultiSite._2010_02',
 'tcsoa.gen.Internal.GlobalMultiSite._2017_05',
 'tcsoa.gen.Internal.GlobalMultiSite._2018_11',
 'tcsoa.gen.Internal.GlobalMultiSite._2020_01',
 'tcsoa.gen.Internal.IcsAw',
 'tcsoa.gen.Internal.IcsAw._2017_06',
 'tcsoa.gen.Internal.IcsAw._2017_12',
 'tcsoa.gen.Internal.IcsAw._2018_05',
 'tcsoa.gen.Internal.IcsAw._2018_12',
 'tcsoa.gen.Internal.IcsAw._2019_06',
 'tcsoa.gen.Internal.IcsAw._2019_12',
 'tcsoa.gen.Internal.ImportExport',
 'tcsoa.gen.Internal.ImportExport._2010_04',
 'tcsoa.gen.Internal.ImportExport._2017_11',
 'tcsoa.gen.Internal.ImportExport._2018_06',
 'tcsoa.gen.Internal.Integration',
 'tcsoa.gen.Internal.Integration._2007_06',
 'tcsoa.gen.Internal.Integration._2008_06',
 'tcsoa.gen.Internal.Manufacturing',
 'tcsoa.gen.Internal.Manufacturing._2008_12',
 'tcsoa.gen.Internal.Manufacturing._2011_12',
 'tcsoa.gen.Internal.Manufacturing._2012_09',
 'tcsoa.gen.Internal.Manufacturing._2014_06',
 'tcsoa.gen.Internal.Manufacturing._2014_12',
 'tcsoa.gen.Internal.Manufacturing._2015_03',
 'tcsoa.gen.Internal.Manufacturing._2015_10',
 'tcsoa.gen.Internal.Manufacturing._2016_09',
 'tcsoa.gen.Internal.Manufacturing._2017_05',
 'tcsoa.gen.Internal.Manufacturing._2017_11',
 'tcsoa.gen.Internal.Manufacturing._2018_11',
 'tcsoa.gen.Internal.Manufacturing._2019_06',
 'tcsoa.gen.Internal.Manufacturing._2020_01',
 'tcsoa.gen.Internal.Manufacturing._2020_04',
 'tcsoa.gen.Internal.Mmv',
 'tcsoa.gen.Internal.Mmv._2012_09',
 'tcsoa.gen.Internal.MultiSite',
 'tcsoa.gen.Internal.MultiSite._2007_06',
 'tcsoa.gen.Internal.MultiSite._2011_06',
 'tcsoa.gen.Internal.MultiSite._2012_02',
 'tcsoa.gen.Internal.MultiSite._2017_11',
 'tcsoa.gen.Internal.MultiSite._2018_06',
 'tcsoa.gen.Internal.MultiSite._2020_12',
 'tcsoa.gen.Internal.Notification',
 'tcsoa.gen.Internal.Notification._2014_10',
 'tcsoa.gen.Internal.Notification._2015_03',
 'tcsoa.gen.Internal.Notification._2015_10',
 'tcsoa.gen.Internal.Notification._2017_11',
 'tcsoa.gen.Internal.OccMgmt',
 'tcsoa.gen.Internal.OccMgmt._2020_05',
 'tcsoa.gen.Internal.OccMgmt._2020_12',
 'tcsoa.gen.Internal.ProductConfiguratorAw',
 'tcsoa.gen.Internal.ProductConfiguratorAw._2017_12',
 'tcsoa.gen.Internal.ProductConfiguratorAw._2018_05',
 'tcsoa.gen.Internal.ProductConfiguratorAw._2020_05',
 'tcsoa.gen.Internal.ProductConfiguratorAw._2020_12',
 'tcsoa.gen.Internal.ProjectManagement',
 'tcsoa.gen.Internal.ProjectManagement._2007_01',
 'tcsoa.gen.Internal.ProjectManagement._2007_06',
 'tcsoa.gen.Internal.ProjectManagement._2008_06',
 'tcsoa.gen.Internal.ProjectManagement._2009_10',
 'tcsoa.gen.Internal.ProjectManagement._2010_04',
 'tcsoa.gen.Internal.ProjectManagement._2011_06',
 'tcsoa.gen.Internal.ProjectManagement._2012_02',
 'tcsoa.gen.Internal.ProjectManagement._2014_10',
 'tcsoa.gen.Internal.ProjectManagementAw',
 'tcsoa.gen.Internal.ProjectManagementAw._2019_12',
 'tcsoa.gen.Internal.Query',
 'tcsoa.gen.Internal.Query._2008_06',
 'tcsoa.gen.Internal.Query._2012_02',
 'tcsoa.gen.Internal.Query._2013_05',
 'tcsoa.gen.Internal.Query._2014_10',
 'tcsoa.gen.Internal.Rdv',
 'tcsoa.gen.Internal.Rdv._2007_06',
 'tcsoa.gen.Internal.Rdv._2007_09',
 'tcsoa.gen.Internal.Rdv._2008_03',
 'tcsoa.gen.Internal.Rdv._2009_01',
 'tcsoa.gen.Internal.Rdv._2009_04',
 'tcsoa.gen.Internal.Rdv._2009_05',
 'tcsoa.gen.Internal.Rdv._2010_04',
 'tcsoa.gen.Internal.Reports',
 'tcsoa.gen.Internal.Reports._2007_06',
 'tcsoa.gen.Internal.Requirementsmanagement',
 'tcsoa.gen.Internal.Requirementsmanagement._2009_10',
 'tcsoa.gen.Internal.Requirementsmanagement._2012_02',
 'tcsoa.gen.Internal.Requirementsmanagement._2012_10',
 'tcsoa.gen.Internal.RevRuleMgmt',
 'tcsoa.gen.Internal.RevRuleMgmt._2019_12',
 'tcsoa.gen.Internal.Search',
 'tcsoa.gen.Internal.Search._2020_12',
 'tcsoa.gen.Internal.Security',
 'tcsoa.gen.Internal.Security._2017_12',
 'tcsoa.gen.Internal.Structure',
 'tcsoa.gen.Internal.Structure._2020_12',
 'tcsoa.gen.Internal.StructureManagement',
 'tcsoa.gen.Internal.StructureManagement._2007_06',
 'tcsoa.gen.Internal.StructureManagement._2007_12',
 'tcsoa.gen.Internal.StructureManagement._2008_03',
 'tcsoa.gen.Internal.StructureManagement._2008_05',
 'tcsoa.gen.Internal.StructureManagement._2008_06',
 'tcsoa.gen.Internal.StructureManagement._2009_10',
 'tcsoa.gen.Internal.StructureManagement._2010_04',
 'tcsoa.gen.Internal.StructureManagement._2010_09',
 'tcsoa.gen.Internal.StructureManagement._2011_06',
 'tcsoa.gen.Internal.StructureManagement._2012_02',
 'tcsoa.gen.Internal.StructureManagement._2012_09',
 'tcsoa.gen.Internal.StructureManagement._2013_05',
 'tcsoa.gen.Internal.StructureManagement._2013_12',
 'tcsoa.gen.Internal.StructureManagement._2014_12',
 'tcsoa.gen.Internal.StructureManagement._2015_10',
 'tcsoa.gen.Internal.StructureManagement._2016_03',
 'tcsoa.gen.Internal.StructureManagement._2016_10',
 'tcsoa.gen.Internal.StructureManagement._2017_05',
 'tcsoa.gen.Internal.StructureManagement._2018_11',
 'tcsoa.gen.Internal.StructureManagement._2020_05',
 'tcsoa.gen.Internal.TCXMLImportExport',
 'tcsoa.gen.Internal.TCXMLImportExport._2020_12',
 'tcsoa.gen.Internal.Translation',
 'tcsoa.gen.Internal.Translation._2007_06',
 'tcsoa.gen.Internal.UiConfig',
 'tcsoa.gen.Internal.UiConfig._2014_11',
 'tcsoa.gen.Internal.Validation',
 'tcsoa.gen.Internal.Validation._2007_06',
 'tcsoa.gen.Internal.Validation._2008_06',
 'tcsoa.gen.Internal.Validation._2012_02',
 'tcsoa.gen.Internal.VendorManagementAW',
 'tcsoa.gen.Internal.VendorManagementAW._2019_12',
 'tcsoa.gen.Internal.VendorManagementAW._2020_05',
 'tcsoa.gen.Internal.VendorManagementAW._2020_12',
 'tcsoa.gen.Internal.Vendormanagement',
 'tcsoa.gen.Internal.Vendormanagement._2008_05',
 'tcsoa.gen.Internal.Vendormanagement._2008_06',
 'tcsoa.gen.Internal.Visualization',
 'tcsoa.gen.Internal.Visualization._2008_06',
 'tcsoa.gen.Internal.Visualization._2010_04',
 'tcsoa.gen.Internal.Visualization._2010_09',
 'tcsoa.gen.Internal.Visualization._2011_12',
 'tcsoa.gen.Internal.Visualization._2012_10',
 'tcsoa.gen.Internal.Visualization._2017_05',
 'tcsoa.gen.Internal.Visualization._2018_11',
 'tcsoa.gen.Internal.Workflow',
 'tcsoa.gen.Internal.Workflow._2013_05',
 'tcsoa.gen.Internal.Workflow._2017_11',
 'tcsoa.gen.Internal.Workflowaw',
 'tcsoa.gen.Internal.Workflowaw._2020_12',
 'tcsoa.gen.Internal.XlsBom',
 'tcsoa.gen.Internal.XlsBom._2020_12',
 'tcsoa.gen.Internal_AWS2',
 'tcsoa.gen.Internal_AWS2._2012_10',
 'tcsoa.gen.Internal_AWS2._2013_12',
 'tcsoa.gen.Internal_AWS2._2014_11',
 'tcsoa.gen.Internal_AWS2._2015_03',
 'tcsoa.gen.Internal_AWS2._2015_10',
 'tcsoa.gen.Internal_AWS2._2016_03',
 'tcsoa.gen.Internal_AWS2._2016_04',
 'tcsoa.gen.Internal_AWS2._2016_12',
 'tcsoa.gen.Internal_AWS2._2017_06',
 'tcsoa.gen.Internal_AWS2._2017_12',
 'tcsoa.gen.Internal_AWS2._2018_05',
 'tcsoa.gen.Internal_AWS2._2018_12',
 'tcsoa.gen.Internal_AWS2._2019_06',
 'tcsoa.gen.Internal_AWS2._2019_12',
 'tcsoa.gen.Internal_AWS2._2020_05',
 'tcsoa.gen.Internal_AWS2._2020_12',
 'tcsoa.gen.Internal_ActiveWorkspaceBom',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2012_10',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2015_03',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2015_07',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2015_10',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2016_03',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2017_06',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2017_12',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2018_05',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2018_12',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2019_06',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2019_12',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2020_05',
 'tcsoa.gen.Internal_ActiveWorkspaceBom._2020_12',
 'tcsoa.gen.Internal_ActiveWorkspaceVis',
 'tcsoa.gen.Internal_ActiveWorkspaceVis._2014_11',
 'tcsoa.gen.Internal_ActiveWorkspaceVis._2015_03',
 'tcsoa.gen.Internal_ActiveWorkspaceVis._2018_05',
 'tcsoa.gen.Internal_Administration',
 'tcsoa.gen.Internal_Administration._2007_06',
 'tcsoa.gen.Internal_Administration._2008_06',
 'tcsoa.gen.Internal_Administration._2009_10',
 'tcsoa.gen.Internal_Administration._2011_06',
 'tcsoa.gen.Internal_Administration._2012_10',
 'tcsoa.gen.Internal_Administration._2013_05',
 'tcsoa.gen.Internal_Administration._2014_10',
 'tcsoa.gen.Internal_Administration._2015_10',
 'tcsoa.gen.Internal_Administration._2016_09',
 'tcsoa.gen.Internal_Administration._2017_11',
 'tcsoa.gen.Internal_Administration._2018_06',
 'tcsoa.gen.Internal_Administration._2018_11',
 'tcsoa.gen.Internal_Administration._2019_06',
 'tcsoa.gen.Internal_Ai',
 'tcsoa.gen.Internal_Ai._2008_06',
 'tcsoa.gen.Internal_Ai._2016_03',
 'tcsoa.gen.Internal_Ai._2016_04',
 'tcsoa.gen.Internal_AuditManager',
 'tcsoa.gen.Internal_AuditManager._2012_09',
 'tcsoa.gen.Internal_BusinessModeler',
 'tcsoa.gen.Internal_BusinessModeler._2007_01',
 'tcsoa.gen.Internal_BusinessModeler._2010_04',
 'tcsoa.gen.Internal_BusinessModeler._2010_09',
 'tcsoa.gen.Internal_BusinessModeler._2011_06',
 'tcsoa.gen.Internal_BusinessModeler._2013_05',
 'tcsoa.gen.Internal_Cad',
 'tcsoa.gen.Internal_Cad._2007_12',
 'tcsoa.gen.Internal_Cad._2008_03',
 'tcsoa.gen.Internal_Cad._2008_05',
 'tcsoa.gen.Internal_Cad._2008_06',
 'tcsoa.gen.Internal_Cad._2010_04',
 'tcsoa.gen.Internal_Cad._2013_05',
 'tcsoa.gen.Internal_Cad._2017_05',
 'tcsoa.gen.Internal_Cae',
 'tcsoa.gen.Internal_Cae._2009_10',
 'tcsoa.gen.Internal_Cae._2011_06',
 'tcsoa.gen.Internal_Cae._2012_02',
 'tcsoa.gen.Internal_Cae._2012_09',
 'tcsoa.gen.Internal_Cae._2013_05',
 'tcsoa.gen.Internal_Cae._2013_12',
 'tcsoa.gen.Internal_Cae._2014_06',
 'tcsoa.gen.Internal_ChangeManagement',
 'tcsoa.gen.Internal_ChangeManagement._2012_10',
 'tcsoa.gen.Internal_ChangeManagement._2015_03',
 'tcsoa.gen.Internal_ChangeManagement._2020_01',
 'tcsoa.gen.Internal_Classification',
 'tcsoa.gen.Internal_Classification._2009_10',
 'tcsoa.gen.Internal_Classification._2017_05',
 'tcsoa.gen.Internal_Classification._2018_11',
 'tcsoa.gen.Internal_Classification._2020_04',
 'tcsoa.gen.Internal_CodeCoverage',
 'tcsoa.gen.Internal_CodeCoverage._2011_06',
 'tcsoa.gen.Internal_ConfigFilterCriteria',
 'tcsoa.gen.Internal_ConfigFilterCriteria._2013_12',
 'tcsoa.gen.Internal_Configurator',
 'tcsoa.gen.Internal_Configurator._2014_06',
 'tcsoa.gen.Internal_Configurator._2014_12',
 'tcsoa.gen.Internal_Configurator._2015_03',
 'tcsoa.gen.Internal_Configurator._2015_10',
 'tcsoa.gen.Internal_Configurator._2016_09',
 'tcsoa.gen.Internal_Configurator._2017_11',
 'tcsoa.gen.Internal_Configurator._2018_06',
 'tcsoa.gen.Internal_Configurator._2018_11',
 'tcsoa.gen.Internal_Core',
 'tcsoa.gen.Internal_Core._2006_03',
 'tcsoa.gen.Internal_Core._2007_01',
 'tcsoa.gen.Internal_Core._2007_05',
 'tcsoa.gen.Internal_Core._2007_06',
 'tcsoa.gen.Internal_Core._2007_09',
 'tcsoa.gen.Internal_Core._2007_12',
 'tcsoa.gen.Internal_Core._2008_03',
 'tcsoa.gen.Internal_Core._2008_06',
 'tcsoa.gen.Internal_Core._2009_10',
 'tcsoa.gen.Internal_Core._2010_04',
 'tcsoa.gen.Internal_Core._2010_09',
 'tcsoa.gen.Internal_Core._2011_06',
 'tcsoa.gen.Internal_Core._2012_02',
 'tcsoa.gen.Internal_Core._2012_09',
 'tcsoa.gen.Internal_Core._2012_10',
 'tcsoa.gen.Internal_Core._2013_05',
 'tcsoa.gen.Internal_Core._2014_10',
 'tcsoa.gen.Internal_Core._2014_11',
 'tcsoa.gen.Internal_Core._2016_10',
 'tcsoa.gen.Internal_Core._2017_05',
 'tcsoa.gen.Internal_Core._2017_11',
 'tcsoa.gen.Internal_Core._2018_06',
 'tcsoa.gen.Internal_Core._2018_11',
 'tcsoa.gen.Internal_Core._2018_12',
 'tcsoa.gen.Internal_Core._2020_01',
 'tcsoa.gen.Internal_Core._2020_04',
 'tcsoa.gen.Internal_DebugMonitor',
 'tcsoa.gen.Internal_DebugMonitor._2011_06',
 'tcsoa.gen.Internal_DebugMonitor._2014_06',
 'tcsoa.gen.Internal_DebugMonitor._2015_07',
 'tcsoa.gen.Internal_DebugMonitor._2015_10',
 'tcsoa.gen.Internal_DebugMonitor._2019_06',
 'tcsoa.gen.Internal_DocMgmtAw',
 'tcsoa.gen.Internal_DocMgmtAw._2019_06',
 'tcsoa.gen.Internal_DocMgmtAw._2019_12',
 'tcsoa.gen.Internal_DocumentManagement',
 'tcsoa.gen.Internal_DocumentManagement._2008_06',
 'tcsoa.gen.Internal_DocumentManagement._2013_05',
 'tcsoa.gen.Internal_DocumentManagement._2013_12',
 'tcsoa.gen.Internal_DocumentManagement._2020_12',
 'tcsoa.gen.Internal_EntCba',
 'tcsoa.gen.Internal_EntCba._2019_12',
 'tcsoa.gen.Internal_Gdis',
 'tcsoa.gen.Internal_Gdis._2006_03',
 'tcsoa.gen.Internal_GlobalMultiSite',
 'tcsoa.gen.Internal_GlobalMultiSite._2007_06',
 'tcsoa.gen.Internal_GlobalMultiSite._2008_06',
 'tcsoa.gen.Internal_GlobalMultiSite._2010_02',
 'tcsoa.gen.Internal_GlobalMultiSite._2010_09',
 'tcsoa.gen.Internal_GlobalMultiSite._2017_05',
 'tcsoa.gen.Internal_GlobalMultiSite._2018_11',
 'tcsoa.gen.Internal_GlobalMultiSite._2020_01',
 'tcsoa.gen.Internal_IcsAw',
 'tcsoa.gen.Internal_IcsAw._2017_06',
 'tcsoa.gen.Internal_IcsAw._2017_12',
 'tcsoa.gen.Internal_IcsAw._2018_05',
 'tcsoa.gen.Internal_IcsAw._2018_12',
 'tcsoa.gen.Internal_IcsAw._2019_06',
 'tcsoa.gen.Internal_IcsAw._2019_12',
 'tcsoa.gen.Internal_ImportExport',
 'tcsoa.gen.Internal_ImportExport._2010_04',
 'tcsoa.gen.Internal_ImportExport._2017_05',
 'tcsoa.gen.Internal_ImportExport._2017_11',
 'tcsoa.gen.Internal_ImportExport._2018_06',
 'tcsoa.gen.Internal_Integration',
 'tcsoa.gen.Internal_Integration._2007_06',
 'tcsoa.gen.Internal_Integration._2008_06',
 'tcsoa.gen.Internal_Manufacturing',
 'tcsoa.gen.Internal_Manufacturing._2008_12',
 'tcsoa.gen.Internal_Manufacturing._2011_12',
 'tcsoa.gen.Internal_Manufacturing._2012_09',
 'tcsoa.gen.Internal_Manufacturing._2013_12',
 'tcsoa.gen.Internal_Manufacturing._2014_06',
 'tcsoa.gen.Internal_Manufacturing._2014_12',
 'tcsoa.gen.Internal_Manufacturing._2015_03',
 'tcsoa.gen.Internal_Manufacturing._2015_10',
 'tcsoa.gen.Internal_Manufacturing._2016_03',
 'tcsoa.gen.Internal_Manufacturing._2016_09',
 'tcsoa.gen.Internal_Manufacturing._2017_05',
 'tcsoa.gen.Internal_Manufacturing._2017_11',
 'tcsoa.gen.Internal_Manufacturing._2018_11',
 'tcsoa.gen.Internal_Manufacturing._2019_06',
 'tcsoa.gen.Internal_Manufacturing._2020_01',
 'tcsoa.gen.Internal_Manufacturing._2020_04',
 'tcsoa.gen.Internal_Mmv',
 'tcsoa.gen.Internal_Mmv._2012_09',
 'tcsoa.gen.Internal_MultiSite',
 'tcsoa.gen.Internal_MultiSite._2007_06',
 'tcsoa.gen.Internal_MultiSite._2011_06',
 'tcsoa.gen.Internal_MultiSite._2012_02',
 'tcsoa.gen.Internal_MultiSite._2017_11',
 'tcsoa.gen.Internal_MultiSite._2018_06',
 'tcsoa.gen.Internal_MultiSite._2020_12',
 'tcsoa.gen.Internal_Notification',
 'tcsoa.gen.Internal_Notification._2014_10',
 'tcsoa.gen.Internal_Notification._2015_03',
 'tcsoa.gen.Internal_Notification._2015_10',
 'tcsoa.gen.Internal_Notification._2017_11',
 'tcsoa.gen.Internal_OccMgmt',
 'tcsoa.gen.Internal_OccMgmt._2020_05',
 'tcsoa.gen.Internal_OccMgmt._2020_12',
 'tcsoa.gen.Internal_ProductConfiguratorAw',
 'tcsoa.gen.Internal_ProductConfiguratorAw._2017_12',
 'tcsoa.gen.Internal_ProductConfiguratorAw._2018_05',
 'tcsoa.gen.Internal_ProductConfiguratorAw._2020_05',
 'tcsoa.gen.Internal_ProductConfiguratorAw._2020_12',
 'tcsoa.gen.Internal_ProjectManagement',
 'tcsoa.gen.Internal_ProjectManagement._2007_01',
 'tcsoa.gen.Internal_ProjectManagement._2007_06',
 'tcsoa.gen.Internal_ProjectManagement._2008_06',
 'tcsoa.gen.Internal_ProjectManagement._2009_10',
 'tcsoa.gen.Internal_ProjectManagement._2010_04',
 'tcsoa.gen.Internal_ProjectManagement._2011_06',
 'tcsoa.gen.Internal_ProjectManagement._2012_02',
 'tcsoa.gen.Internal_ProjectManagement._2014_10',
 'tcsoa.gen.Internal_ProjectManagementAw',
 'tcsoa.gen.Internal_ProjectManagementAw._2019_12',
 'tcsoa.gen.Internal_Query',
 'tcsoa.gen.Internal_Query._2008_06',
 'tcsoa.gen.Internal_Query._2012_02',
 'tcsoa.gen.Internal_Query._2013_05',
 'tcsoa.gen.Internal_Query._2014_10',
 'tcsoa.gen.Internal_Rdv',
 'tcsoa.gen.Internal_Rdv._2007_06',
 'tcsoa.gen.Internal_Rdv._2007_09',
 'tcsoa.gen.Internal_Rdv._2008_03',
 'tcsoa.gen.Internal_Rdv._2009_01',
 'tcsoa.gen.Internal_Rdv._2009_04',
 'tcsoa.gen.Internal_Rdv._2009_05',
 'tcsoa.gen.Internal_Rdv._2010_04',
 'tcsoa.gen.Internal_Reports',
 'tcsoa.gen.Internal_Reports._2007_06',
 'tcsoa.gen.Internal_Requirementsmanagement',
 'tcsoa.gen.Internal_Requirementsmanagement._2009_10',
 'tcsoa.gen.Internal_Requirementsmanagement._2012_02',
 'tcsoa.gen.Internal_Requirementsmanagement._2012_10',
 'tcsoa.gen.Internal_RevRuleMgmt',
 'tcsoa.gen.Internal_RevRuleMgmt._2019_12',
 'tcsoa.gen.Internal_Search',
 'tcsoa.gen.Internal_Search._2020_12',
 'tcsoa.gen.Internal_Security',
 'tcsoa.gen.Internal_Security._2017_12',
 'tcsoa.gen.Internal_Structure',
 'tcsoa.gen.Internal_Structure._2020_12',
 'tcsoa.gen.Internal_StructureManagement',
 'tcsoa.gen.Internal_StructureManagement._2007_06',
 'tcsoa.gen.Internal_StructureManagement._2007_12',
 'tcsoa.gen.Internal_StructureManagement._2008_03',
 'tcsoa.gen.Internal_StructureManagement._2008_05',
 'tcsoa.gen.Internal_StructureManagement._2008_06',
 'tcsoa.gen.Internal_StructureManagement._2009_10',
 'tcsoa.gen.Internal_StructureManagement._2010_04',
 'tcsoa.gen.Internal_StructureManagement._2010_09',
 'tcsoa.gen.Internal_StructureManagement._2011_06',
 'tcsoa.gen.Internal_StructureManagement._2012_02',
 'tcsoa.gen.Internal_StructureManagement._2012_09',
 'tcsoa.gen.Internal_StructureManagement._2013_05',
 'tcsoa.gen.Internal_StructureManagement._2013_12',
 'tcsoa.gen.Internal_StructureManagement._2014_12',
 'tcsoa.gen.Internal_StructureManagement._2015_10',
 'tcsoa.gen.Internal_StructureManagement._2016_03',
 'tcsoa.gen.Internal_StructureManagement._2016_10',
 'tcsoa.gen.Internal_StructureManagement._2017_05',
 'tcsoa.gen.Internal_StructureManagement._2018_11',
 'tcsoa.gen.Internal_StructureManagement._2019_06',
 'tcsoa.gen.Internal_StructureManagement._2020_05',
 'tcsoa.gen.Internal_TCXMLImportExport',
 'tcsoa.gen.Internal_TCXMLImportExport._2020_12',
 'tcsoa.gen.Internal_Translation',
 'tcsoa.gen.Internal_Translation._2007_06',
 'tcsoa.gen.Internal_UiConfig',
 'tcsoa.gen.Internal_UiConfig._2014_11',
 'tcsoa.gen.Internal_Validation',
 'tcsoa.gen.Internal_Validation._2007_06',
 'tcsoa.gen.Internal_Validation._2008_06',
 'tcsoa.gen.Internal_Validation._2010_04',
 'tcsoa.gen.Internal_Validation._2012_02',
 'tcsoa.gen.Internal_VendorManagementAW',
 'tcsoa.gen.Internal_VendorManagementAW._2019_12',
 'tcsoa.gen.Internal_VendorManagementAW._2020_05',
 'tcsoa.gen.Internal_VendorManagementAW._2020_12',
 'tcsoa.gen.Internal_Vendormanagement',
 'tcsoa.gen.Internal_Vendormanagement._2008_05',
 'tcsoa.gen.Internal_Vendormanagement._2008_06',
 'tcsoa.gen.Internal_Visualization',
 'tcsoa.gen.Internal_Visualization._2008_06',
 'tcsoa.gen.Internal_Visualization._2010_04',
 'tcsoa.gen.Internal_Visualization._2010_09',
 'tcsoa.gen.Internal_Visualization._2011_12',
 'tcsoa.gen.Internal_Visualization._2012_10',
 'tcsoa.gen.Internal_Visualization._2017_05',
 'tcsoa.gen.Internal_Visualization._2018_11',
 'tcsoa.gen.Internal_Workflow',
 'tcsoa.gen.Internal_Workflow._2013_05',
 'tcsoa.gen.Internal_Workflow._2017_11',
 'tcsoa.gen.Internal_Workflowaw',
 'tcsoa.gen.Internal_Workflowaw._2020_12',
 'tcsoa.gen.Internal_XlsBom',
 'tcsoa.gen.Internal_XlsBom._2020_12',
 'tcsoa.gen.Manufacturing',
 'tcsoa.gen.Manufacturing._2008_06',
 'tcsoa.gen.Manufacturing._2008_12',
 'tcsoa.gen.Manufacturing._2009_06',
 'tcsoa.gen.Manufacturing._2009_10',
 'tcsoa.gen.Manufacturing._2010_09',
 'tcsoa.gen.Manufacturing._2011_06',
 'tcsoa.gen.Manufacturing._2012_02',
 'tcsoa.gen.Manufacturing._2012_09',
 'tcsoa.gen.Manufacturing._2013_05',
 'tcsoa.gen.Manufacturing._2013_12',
 'tcsoa.gen.Manufacturing._2014_06',
 'tcsoa.gen.Manufacturing._2014_12',
 'tcsoa.gen.Manufacturing._2015_03',
 'tcsoa.gen.Manufacturing._2015_10',
 'tcsoa.gen.Manufacturing._2016_03',
 'tcsoa.gen.Manufacturing._2017_05',
 'tcsoa.gen.Manufacturing._2017_11',
 'tcsoa.gen.Manufacturing._2018_06',
 'tcsoa.gen.Manufacturing._2018_11',
 'tcsoa.gen.Manufacturing._2019_06',
 'tcsoa.gen.Multisite',
 'tcsoa.gen.Multisite._2007_06',
 'tcsoa.gen.Multisite._2011_06',
 'tcsoa.gen.Multisite._2014_10',
 'tcsoa.gen.Multisite._2019_06',
 'tcsoa.gen.Notification',
 'tcsoa.gen.Notification._2014_10',
 'tcsoa.gen.OfficeOnline',
 'tcsoa.gen.OfficeOnline._2017_11',
 'tcsoa.gen.Participant',
 'tcsoa.gen.Participant._2018_11',
 'tcsoa.gen.ProjectManagement',
 'tcsoa.gen.ProjectManagement._2007_01',
 'tcsoa.gen.ProjectManagement._2007_06',
 'tcsoa.gen.ProjectManagement._2007_12',
 'tcsoa.gen.ProjectManagement._2008_06',
 'tcsoa.gen.ProjectManagement._2009_10',
 'tcsoa.gen.ProjectManagement._2011_02',
 'tcsoa.gen.ProjectManagement._2011_06',
 'tcsoa.gen.ProjectManagement._2011_12',
 'tcsoa.gen.ProjectManagement._2012_02',
 'tcsoa.gen.ProjectManagement._2012_09',
 'tcsoa.gen.ProjectManagement._2014_06',
 'tcsoa.gen.ProjectManagement._2014_10',
 'tcsoa.gen.ProjectManagement._2015_07',
 'tcsoa.gen.ProjectManagement._2016_04',
 'tcsoa.gen.ProjectManagement._2017_11',
 'tcsoa.gen.ProjectManagement._2018_11',
 'tcsoa.gen.ProjectManagementAw',
 'tcsoa.gen.ProjectManagementAw._2015_07',
 'tcsoa.gen.ProjectManagementAw._2016_12',
 'tcsoa.gen.ProjectManagementAw._2017_06',
 'tcsoa.gen.ProjectManagementAw._2018_12',
 'tcsoa.gen.ProjectManagementAw._2019_06',
 'tcsoa.gen.ProjectManagementAw._2020_05',
 'tcsoa.gen.Qualification',
 'tcsoa.gen.Qualification._2014_06',
 'tcsoa.gen.Query',
 'tcsoa.gen.Query._2006_03',
 'tcsoa.gen.Query._2007_01',
 'tcsoa.gen.Query._2007_06',
 'tcsoa.gen.Query._2007_09',
 'tcsoa.gen.Query._2008_06',
 'tcsoa.gen.Query._2010_04',
 'tcsoa.gen.Query._2010_09',
 'tcsoa.gen.Query._2012_10',
 'tcsoa.gen.Query._2013_05',
 'tcsoa.gen.Query._2014_11',
 'tcsoa.gen.Query._2018_11',
 'tcsoa.gen.Query._2019_06',
 'tcsoa.gen.Query._2020_04',
 'tcsoa.gen.Rdv',
 'tcsoa.gen.Rdv._2008_05',
 'tcsoa.gen.Rdv._2009_04',
 'tcsoa.gen.Rdv._2010_09',
 'tcsoa.gen.Rdv._2012_09',
 'tcsoa.gen.Rdv._2013_05',
 'tcsoa.gen.RelationshipViewer',
 'tcsoa.gen.RelationshipViewer._2012_10',
 'tcsoa.gen.RelationshipViewer._2014_11',
 'tcsoa.gen.RelationshipViewer._2019_12',
 'tcsoa.gen.Reports',
 'tcsoa.gen.Reports._2007_01',
 'tcsoa.gen.Reports._2007_06',
 'tcsoa.gen.Reports._2008_06',
 'tcsoa.gen.Reports._2008_12',
 'tcsoa.gen.Reports._2010_04',
 'tcsoa.gen.Reports._2015_03',
 'tcsoa.gen.Reports._2015_10',
 'tcsoa.gen.Requirementsmanagement',
 'tcsoa.gen.Requirementsmanagement._2007_01',
 'tcsoa.gen.Requirementsmanagement._2008_06',
 'tcsoa.gen.Requirementsmanagement._2009_10',
 'tcsoa.gen.Requirementsmanagement._2010_09',
 'tcsoa.gen.Requirementsmanagement._2011_06',
 'tcsoa.gen.Requirementsmanagement._2012_09',
 'tcsoa.gen.StructureManagement',
 'tcsoa.gen.StructureManagement._2007_06',
 'tcsoa.gen.StructureManagement._2008_03',
 'tcsoa.gen.StructureManagement._2008_05',
 'tcsoa.gen.StructureManagement._2008_06',
 'tcsoa.gen.StructureManagement._2008_12',
 'tcsoa.gen.StructureManagement._2010_04',
 'tcsoa.gen.StructureManagement._2010_09',
 'tcsoa.gen.StructureManagement._2011_06',
 'tcsoa.gen.StructureManagement._2012_02',
 'tcsoa.gen.StructureManagement._2012_09',
 'tcsoa.gen.StructureManagement._2012_10',
 'tcsoa.gen.StructureManagement._2013_05',
 'tcsoa.gen.StructureManagement._2014_06',
 'tcsoa.gen.StructureManagement._2014_10',
 'tcsoa.gen.StructureManagement._2014_12',
 'tcsoa.gen.StructureManagement._2015_10',
 'tcsoa.gen.StructureManagement._2016_05',
 'tcsoa.gen.StructureManagement._2016_09',
 'tcsoa.gen.StructureManagement._2017_05',
 'tcsoa.gen.StructureManagement._2018_11',
 'tcsoa.gen.StructureManagement._2019_06',
 'tcsoa.gen.Translation',
 'tcsoa.gen.Translation._2007_06',
 'tcsoa.gen.UiConfig',
 'tcsoa.gen.UiConfig._2014_11',
 'tcsoa.gen.UiConfig._2015_10',
 'tcsoa.gen.Vendormanagement',
 'tcsoa.gen.Vendormanagement._2007_06',
 'tcsoa.gen.Vendormanagement._2008_06',
 'tcsoa.gen.Vendormanagement._2012_02',
 'tcsoa.gen.Vendormanagement._2012_09',
 'tcsoa.gen.Vendormanagement._2016_09',
 'tcsoa.gen.Visualization',
 'tcsoa.gen.Visualization._2011_02',
 'tcsoa.gen.Visualization._2013_05',
 'tcsoa.gen.Visualization._2013_12',
 'tcsoa.gen.Visualization._2016_03',
 'tcsoa.gen.WProxy',
 'tcsoa.gen.WProxy._2014_10',
 'tcsoa.gen.Workflow',
 'tcsoa.gen.Workflow._2007_06',
 'tcsoa.gen.Workflow._2008_06',
 'tcsoa.gen.Workflow._2010_09',
 'tcsoa.gen.Workflow._2012_10',
 'tcsoa.gen.Workflow._2013_05',
 'tcsoa.gen.Workflow._2014_06',
 'tcsoa.gen.Workflow._2014_10',
 'tcsoa.gen.Workflow._2015_07',
 'tcsoa.gen.Workflow._2019_06',
 'tcsoa.gen.Workflow._2020_01']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.13,<2.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'tcsoa',
    'version': '0.10.1',
    'description': 'A framework generated for the purpose of consuming Teamcenter™ services via Python.',
    'long_description': 'None',
    'author': 'Alexander Haas',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
