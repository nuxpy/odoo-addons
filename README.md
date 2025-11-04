[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-%23842029)](https://www.gnu.org/licenses/lgpl-3.0)
[![Static Badge](https://img.shields.io/badge/Website-nuxpy-blue)](https://www.nuxpy.com/)
[![Static Badge](https://img.shields.io/badge/Wiki-nuxpy-green)](https://www.wiki.nuxpy.com/)

# odoo-addons

## Tag and module name from Odoo:

Tags are used to prefix your commit. They should be one of the following

* [FIX] for bug fixes: mostly used in stable version but also valid if you are fixing a recent bug in development version;
* [REF] for refactoring: when a feature is heavily rewritten;
* [ADD] for adding new modules;
* [REM] for removing resources: removing dead code, removing views, removing modules, …;
* [REV] for reverting commits: if a commit causes issues or is not wanted reverting it is done using this tag;
* [MOV] for moving files: use git move and do not change content of moved file otherwise Git may loose track and history of the file; also used when moving code from one file to another;
* [REL] for release commits: new major or minor stable versions;
* [IMP] for improvements: most of the changes done in development version are incremental improvements not related to another tag;
* [MERGE] for merge commits: used in forward port of bug fixes but also as main commit for feature involving several separated commits;
* [CLA] for signing the Odoo Individual Contributor License;
* [I18N] for changes in translation files;
* [PERF] for performance patches;

After tag comes the modified module name. Use the technical name as functional name may change with time. If several modules are modified, list them or use various to tell it is cross-modules. Unless really required or easier avoid modifying code across several modules in the same commit. Understanding module history may become difficult.
