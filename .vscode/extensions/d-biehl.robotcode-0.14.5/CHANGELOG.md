# Change Log

All notable changes to the "robotcode" extension will be documented in this file.

## [Unreleased]
- none so far
##  0.14.5

- Improve analysing, find references and renaming of environment variables
- Optimize reference handling.
  - This allows updating references when creating and deleting files, if necessary.

##  0.14.4

- Correct resolving paths for test execution

##  0.14.3

- Optimize locking
- Speedup collect available testcases

##  0.14.2

- Add sponsor to package

##  0.14.1

- Connection to the debugger stabilized.

##  0.14.0

- Implement inlay hints for import namespaces and parameter names
  - by default inlay hints for robotcode are only showed if you press <kbd>CONTROL</kbd>+<kbd>ALT</kbd>
  - there are 2 new settings
    `robotcode.inlayHints.parameterNames` and `robotcode.inlayHints.namespaces` where you can enable/disable the inline hints
##  0.13.28

- Remove `--language` argument if using robot < 6
  - fixes [#84](https://github.com/d-biehl/robotcode/issues/84)

##  0.13.27

- Remote Debugging

  - by installing `robotcode` via pip in your environment, you can now run the `robotcode.debugger` (see `--help` for help) from command line and attach VSCode via a remote launch config
  - more documentation comming soon.
  - closes [#86](https://github.com/d-biehl/robotcode/issues/86)

##  0.13.26

- none so far

##  0.13.25

- none so far

##  0.13.24

- The code action "Show documentation" now works for all positions where a keyword can be used or defined
- The code action "Show documentation" now respects the theme activated in VSCode. (dark, light)

##  0.13.23

- Support for Robocop >= 2.6
- Support for Tidy >= 3.3
- Speed improvements

##  0.13.22

- none so far

##  0.13.21

- none so far

##  0.13.20

- Reimplement workspace analysis
- Optimize the search for unused references

##  0.13.19

- Add a the setting `robotcode.completion.filterDefaultLanguage` to filter english language in completion, if there is another language defined for workspace or in file
- Correct naming for setting `robotcode.syntax.sectionStyle` to `robotcode.completion.headerStyle`
- Filter singular header forms for robotframework >= 6

##  0.13.18

- none so far

##  0.13.17

- Support for simple values (number, bool, str) from variable and yaml files
- Shortened representation of variable values in hover

##  0.13.16

- none so far

##  0.13.15

- none so far

##  0.13.14

- Documentation server now works also in remote and web versions of VSCode like [gitpod.io](https://gitpod.io/) and [GitHub CodeSpaces](https://github.com/features/codespaces)

##  0.13.13

- add colors to debug console
- fix resolving of ${CURDIR} in variables
- Open Documentation action now resolves variables correctly and works on resource files

##  0.13.12

- none so far

##  0.13.11

- none so far

##  0.13.10

- Correct reporting of loading built-in modules errors

##  0.13.9

- Correct analysing of "Run Keyword If"
  - fixes [#80](https://github.com/d-biehl/robotcode/issues/80)

##  0.13.8

- Support for Robocop >= 2.4
- Rework handling of launching and debugging tests
  - fixes [#54](https://github.com/d-biehl/robotcode/issues/54)
  - a launch configuration can now have a `purpose`:
    - `test`: Use this configuration when running or debugging tests.
    - `default`: Use this configuration as default for all other configurations.
- Finetuning libdoc generation and code completion
  - support for reST documentions
    - `docutils` needs to be installed
    - show documentations at library and resource import completions
- Experimental support for Source action `Open Documentation`
  - left click on a resource or library import, select Source Action and then "Open Documentation"
  - a browser opens left of the document and shows the full documentation of the library
  - works also an keyword calls
  - Tip: bind "Source Action..." to a keyboard short cut, i.e <kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>.</kbd>

##  0.13.7

- Don't explicitly set suites to failed if there is an empty failed message
  - fixes [#76](https://github.com/d-biehl/robotcode/issues/76)

##  0.13.6

- Extensive adjustments for multiple language support for RobotFramework 5.1, BDD prefixes now works correctly for mixed languages
- New deprecated message for tags that start with hyphen, RF 5.1

##  0.13.5

- Some fixes in analysing and highlightning

##  0.13.4

- none so far

##  0.13.3

- Highlight localized robot files (RobotFramework >= 5.1)

##  0.13.2

- Support for robotidy 3.0
- References are now collected at source code analyze phase
  - this speeds up thinks like find references/renaming/highlight and so on

##  0.13.1

- Switching to LSP Client 8.0.0 requires a VSCode version >= 1.67
- Create snippets for embedded argument keywords

##  0.13.0

- Some corrections in highlightning to provide better bracket matching in arguments

##  0.12.1

- Implement API Changes for RobotTidy >= 2.2
  - fixes [#55](https://github.com/d-biehl/robotcode/issues/55)
- Switch to new LSP Protocol Version 3.17 and vscode-languageclient 8.0.0
- Disable 4SpacesTab if [GitHub CoPilot](https://copilot.github.com/) is showing inline suggestions
  - Thanks: @Snooz82

##  0.12.0

- Find references, highlight references and rename for tags
- Correct handling of keyword only arguments
- Fix the occurrence of spontaneous deadlocks

##  0.11.17

### added

- Information about possible circular imports
  - if one resource file imports another resource file and vice versa an information message is shown in source code and problems list
- References for arguments also finds named arguments

##  0.11.16

- none so far

##  0.11.15

- none so far

##  0.11.14

- none so far

##  0.11.13

- none so far

##  0.11.12

### added

- Reference CodeLenses
  - Code lenses are displayed above the keyword definitions showing the usage of the keyword
  - You can enable/disable this with the new setting `robotcode.analysis.referencesCodeLens`

##  0.11.11

### added

- Project wide code analysis
  - There are some new settings that allow to display project-wide problems:
    - `robotcode.analysis.diagnosticMode` Analysis mode for diagnostics.
      - `openFilesOnly` Analyzes and reports problems only on open files.
      - `workspace` Analyzes and reports problems on all files in the workspace.
      - default: `openFilesOnly`
    - `robotcode.analysis.progressMode` Progress mode for diagnostics.
      - `simple` Show only simple progress messages.
      - `detailed` Show detailed progress messages. Displays the filenames that are currently being analyzed.
      - default: `simple`
    - `robotcode.analysis.maxProjectFileCount` Specifies the maximum number of files for which diagnostics are reported for the whole project/workspace folder. Specifies 0 or less to disable the limit completely.
      - default: `1000`
    - `robotcode.workspace.excludePatterns` Specifies glob patterns for excluding files and folders from analysing by the language server.
- Rework loading and handling source documents
  - this speedups a lot of things like:
    - UI response
    - finding references
    - renaming of keywords and variables
    - loading reloading libraries and resources
  - When you create/rename/delete files, keywords, variables, you get an immediate response in the UI


##  0.11.10

- renaming of keywords and variables
- speedup loading of resources

##  0.11.9

### added

- Return values of keywords calls can be assigned to variables in the debugger console
  - You can call keywords in the debugger console just as you would write your keyword calls in robot files.
    Everything that starts with `'! '` (beware the space) is handled like a keyword call, for example:

    ```
    ! Log  Hello
    ```

    would call the keyword `Log` and writes `Hello` to report.

    ```
    !  Evaluate  1+2
    ```

    calls `Evaluate` and writes the result to the log.

    To assign the result of a keyword to a variable write something like

    ```
    ! ${result}  Evaluate  1+2
    ```

    This will assign the result of the expression to the variable `${result}` in the current execution context.

    A more complex example:

    ```
    ! ${a}  @{c}=  ${b}  Evaluate  "Hello World!!! How do you do?".split(' ')
    ```

    A side effect of this is that the keyword calls are logged in log.html when you continue your debug session.



##  0.11.8

### added
- Test Templates argument analysis
  - Basic usage
  - Templates with embedded arguments
  - Templates with FOR loops and IF/ELSE structures
  - see also [Robot Framework documentation](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates)

##  0.11.7

### added

- optimize restart language clients if configuration changed
- support for progress feature of language server protocol
- correct WHILE snippets
- handle invalid regular expressions in embedded keywords
- correct handling of templates with embedded arguments

##  0.11.6

- none so far

##  0.11.5

- Enable automatic publication of releases on github

##  0.11.4

- none so far

##  0.10.2

- Correct error in find variable references with invalid variables in variable section

##  0.11.3

- Fix selection range on white space

##  0.11.2

- Implement [Selection Range](https://code.visualstudio.com/docs/editor/codebasics#_shrinkexpand-selection) support for Robot Framework
  - starting from a point in the source code you can select the surrounding keyword, block (IF/WHILE,...), test case, test section and so on

##  0.11.1

- Provide better error messages if python and robot environment not matches RobotCode requirements
  - fixes [#40](https://github.com/d-biehl/robotcode/issues/40)
- Correct restart of language server client if python interpreter changed
- Correct start of root test item if `robotcode.robot.paths` is used

##  0.11.0

- Correct find references at token ends
  - If the cursor is at the end of a keyword, for example, the keyword will also be highlighted and the references will be found.

##  0.10.1

### added
- Analyse variables in documentation or metadata settings shows a hint instead of an error if variable is not found
  - fixes [#47](https://github.com/d-biehl/robotcode/issues/47)
- Correct robocop shows false "Invalid number of empty lines between sections"
  - fixes [#46](https://github.com/d-biehl/robotcode/issues/46)]

##  0.10.0

### added
- Introduce setting `robotcode.robot.paths` and correspondend launch config property `paths`
  - Specifies the paths where robot/robotcode should discover test suites. Corresponds to the 'paths' option of robot
- Introduce new RF 5 `${OPTIONS}` variable

##  0.9.6

### added

- Variable analysis, finds undefined variables
  - in variables, also inner variables like ${a+${b}}
  - in inline python expression like ${{$a+$b}}
  - in expression arguments of IF/WHILE statements like $a<$b
  - in BuiltIn keywords which contains an expression or condition argument, like `Evaluate`, `Should Be True`, `Skip If`, ...
- Improve handling of completion for argument definitions
- Support for variable files
  - there is a new setting `robotcode.robot.variableFiles` and corresponding `variableFiles` launch configuration setting
  - this corresponds to the `--variablefile` option from robot

##  0.9.5

### added

- Correct handling of argument definitions wich contains a default value from an allready defined argument

##  0.9.4

### added

- Correct handling of argument definitions wich contains a default value with existing variable with same name
- Implement "Uncaughted Failed Keywords" exception breakpoint
  - from now this is the default breakpoint, means debugger stops only if a keyword failed and it is not called from:
    - BuiltIn.Run Keyword And Expect Error
    - BuiltIn.Run Keyword And Ignore Error
    - BuiltIn.Run Keyword And Warn On Failure
    - BuiltIn.Wait Until Keyword Succeeds
    - BuiltIn.Run Keyword And Continue On Failure
  - partially fixes [#44](https://github.com/d-biehl/robotcode/issues/44)
  - speedup updating test explorers view

##  0.9.3

### added

- Introduce setting `robotcode.robot.variableFiles` and correspondend launch config property `variableFiles`
  - Specifies the variable files for robotframework. Corresponds to the '--variablefile' option of robot.
- Rework debugger termination
  - if you want to stop the current run
    - first click on stop tries to break the run like if you press <kbd>CTRL</kbd>+<kbd>c</kbd> to give the chance that logs and reports are written
    - second click stops/kill execution
- 'None' values are now shown correctly in debugger

##  0.9.2

- none so far

##  0.9.1

### added

- Rework handling keywords from resource files with duplicate names
  - also fixes [#43](https://github.com/d-biehl/robotcode/issues/43)

##  0.9.0

### added

- Optimize collecting model errors
  - also fixes [#42](https://github.com/d-biehl/robotcode/issues/42)
- Add `mode` property to launch configuration and `robotcode.robot.mode` setting for global/workspace/folder
  - define the robot running mode (default, rpa, norpa)
  - corresponds to the '--rpa', '--norpa' option of the robot module.
  - fixes [#21](https://github.com/d-biehl/robotcode/issues/21)

##  0.8.0

### added

- Introduce new version scheme to support pre-release versions of the extension
  - see [README](https://github.com/d-biehl/robotcode#using-pre-release-version)
- Rework handling VSCode test items to ensure all defined tests can be executed, also when they are ambiguous
  - see [#37](https://github.com/d-biehl/robotcode/issues/37)
- Semantic highlighting of new WHILE and EXCEPT options for RF 5.0
- Support for inline IF for RF 5.0
- Support for new BREAK, CONTINUE, RETURN statements for RF 5.0


##  0.7.0

### added

- Add `dryRun` property to launch configuration
- Add "Dry Run" and "Dry Debug" profile to test explorer
  - You can select it via Run/Debug dropdown or Right Click on the "green arrow" before the test case/suite or in test explorer and then "Execute Using Profile"
- Mark using reserved keywords like "Break", "While",... as errors
- Support for NONE in Setup/Teardowns
  - see [here](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown)
  - fixes [#38](https://github.com/d-biehl/robotcode/issues/38)
- Decrease size of extension package
- Sligtly correct displayName and description of VSCode package, for better relevance in Marketplace search
  - See [#39](https://github.com/d-biehl/robotcode/issues/39)

##  0.6.0

### added

- Improved variable analysis
  - In an expression like `${A+'${B+"${F}"}'+'${D}'} ${C}`, every single 'inner' variable will be recognized, you can hover over it, it can be found as reference, you can go to the definition, ...
  - Also in python expressions like `${{$a+$b}}` variables are recognized
  - Support for variables in expression in IF and WHILE statements
    - in something like `$i<5` the variables are recognized
  - Only the name of the variable is used for hovering, goto and ..., not the surrounding ${}
- Support importing variable files as module for RobotFramework 5
- Depending on selected testcase names contains a colon, a semicolon is used as separator of prerunmodifier for executing testcases
    - fixes [#20](https://github.com/d-biehl/robotcode/issues/20)
    - note: i think you should not use colons or semicolon in testcase names ;-)
- Improve Debugger
  - The debugger shows variables as inline values and when hovering, it shows the current variable value not the evaluted expression
  - Variables in the debugger are now resolved correctly and are sorted into Local/Test/Suite and Global variables
  - Fix stepping/halt on breakpoint for IF/ELSE statements if the expression is evaluated as False
  - Rework of stepping and stacktrace in the debugger
    - Only the real steps are displayed in the stack trace
- Optimize keyword matching
  - all keyword references also with embedded arguments + regex are found
  - ambigous embedded keywords are recognized correctly, also with regex
  - speed up finding keyword references
  - fix [#28](https://github.com/d-biehl/robotcode/issues/28)
  - addresses [#24](https://github.com/d-biehl/robotcode/issues/24)
- Ignoring robotcode diagnostics
  - you can put a line comment to disable robotcode diagnostics (i.e errors or warnings) for a single line, like this:

  ```robotcode
  *** Test cases ***
  first
      unknown keyword  a param   # robotcode: ignore
      Run Keyword If    ${True}
      ...    Log    ${Invalid var        # robotcode: ignore
      ...  ELSE
      ...    Unknown keyword  No  # robotcode: ignore
  ```

- Propagate import errors from resources
  - errors like: `Resource file with 'Test Cases' section is invalid` are shown at import statement
  - Note: Robocop has it's own ignore mechanism
- Initialize logging only of "--log" parameter is set from commandline
  - fixes [#30](https://github.com/d-biehl/robotcode/issues/30)
- Optimize loading of imports and collecting keywords
  - this addresses [#24](https://github.com/d-biehl/robotcode/issues/24)
  - one of the big points here is, beware of namespace pollution ;-)
- Full Support for BDD Style keywords
  - includes hover, goto, highlight, references, ...

##  0.5.5

### added

- correct semantic highlightning for "run keywords"
  - now also named arguments in inner keywords are highlighted
- correct handling of parameter names in "run keywords" and inner keywords
- correct handling of resource keywords arguments

##  0.5.4

### added

- Keyword call analysis
  - shows if parameters are missing or too much and so on...
- Highlight of named arguments
- Improve handling of command line variables when resolving variables
- Remove handling of python files to reduce the processor load in certain situations

##  0.5.3

### added

- Resolving static variables, closes [#18](https://github.com/d-biehl/robotcode/issues/18)
  - RobotCode tries to resolve variables that are definied at variables section, command line variables and builtin variables. This make it possible to import libraries/resources/variables with the correct path and parameters.
  Something like this:

  ```robotframework
  *** Settings ***
  Resource          ${RESOURCE_DIR}/some_settings.resource
  Library           alibrary    a_param=${LIB_ARG}
  Resource          ${RESOURCE_DIR}/some_keywords.resource
  ```

  - If you hover over a variable, you will see, if the variable can be resolved

- show quick pick for debug/run configuration
  - if there is no launch configuration selected and you want to run code with "Start Debugging" or "Run without Debugging", robotcode will show you a simple quick pick, where you can select a predefined configuration
- some cosmetic changes in updating Test Explorer
- correct handling of showing inline values and hover over variables in debugger
- correct handling of variable assignment with an "equal" sign
- add more regression tests

##  0.5.2

- some testing

##  0.5.1

### added

- extend README.md
  - added section about style customization
  - extend feature description
- added file icons for robot files
  - starting with VSCode Version 1.64, if the icon theme does not provide an icon for robot files, these icons are used
- add automatic debug configurations
  - you don't need to create a launch.json to run tests in the debugger view
- correct step-in FINALLY in debugger
- test explorer activates now only if there are robot files in workspace folder


##  0.5.0

### added

- Added support for RobotFramework 5.0
  - Debugger supports TRY/EXCEPT, WHILE,... correctly
  - (Semantic)- highlighter detects new statements
  - Formatter not uses internal tidy tool
  - handle EXPECT AS's variables correctly
  - Complete new statements
  - Some completion templates for WHILE, EXCEPT, ...
- Discovering tests is now more error tolerant
- Semantic tokenizing now also detects ERROR and FATAL_ERROR tokens
- some cosmetic corrections in discoring tests

note: RobotFramework 5.0 Alpha 1 has a bug when parsing the EXCEPT AS statement,
so the highlighter does not work correctly with this version.
This bug is fixed in the higher versions.

##  0.4.10

### added

- fix correct reverting documents on document close

##  0.4.9

### added

- correct CHANGELOG

##  0.4.8

### added

- extend [README](https://github.com/d-biehl/robotcode/blob/HEAD/README.md)
- extend highlight of references in fixtures and templates
- correct updating test explorer if files are deleted or reverted
- some cosmetic changes

##  0.4.7

### added

- hover/goto/references/highlight... differentiate between namespace and keyword in keyword calls like "BuiltIn.Log"
- increase test coverage

##  0.4.6
### added

- some small fixes in completion, command line parameters and variable references

##  0.4.5

### added

- correct semantic highlight of variables and settings
- completion window for keywords is now opened only after triggering Ctrl+Space or input of the first character

##  0.4.4

### added

- implement InlineValuesProvider and EvaluatableExpressionProvider in language server

##  0.4.3

### added

- implement find references for libraries, resources, variables import
- implement document highlight for variables and keywords

##  0.4.2

### added

- added support for variables import
  - completion
  - hover
  - goto
  - static and dynamic variables
- correct debugger hover on variables and last fail message
- implement find references for variables


##  0.4.1

### added

- for socket connections now a free port is used
- collect variables and arguments to document symbols
- analysing, highlighting of "Wait Until Keyword Succeeds" and "Repeat Keyword"

##  0.4.0

### added

- Big speed improvements
  - introduce some classes for threadsafe asyncio
- Implement pipe/socket transport for language server
  - default is now pipe transport
- Improve starting, stopping, restarting language server client, if ie. python environment changed, arguments changed or server crashed
- some refactoring to speedup loading and parsing documents
- semantic tokens now highlight
  - builtin keywords
  - run keywords, also nested run keywords
- analysing run keywords now correctly unescape keywords

##  0.3.2

### added

- remove deadlock in resource loading

##  0.3.1

### added

- implement find keyword references
  - closes [#13](https://github.com/d-biehl/robotcode/issues/13)
- improve parsing and analysing of "run keywords ..."
  - closes [#14](https://github.com/d-biehl/robotcode/issues/14)

##  0.3.0

### added

- remove pydantic dependency
    - closes [#11](https://github.com/d-biehl/robotcode/issues/11)
    - big refactoring of LSP and DAP types
- fix overlapping semantic tokens

##  0.2.11

### added

- fix [#10](https://github.com/d-biehl/robotcode/issues/10)
- start implementing more unit tests
- extend hover and goto for variables

##  0.2.10

### added

- extend sematic higlightning
    - builtin library keywords are declared as default_library modifier
    - higlight variables in keyword names and keyword calls
- complete embedded arguments

##  0.2.9

### added

- some correction to load libraries/resources with same name
    - fixes [#9](https://github.com/d-biehl/robotcode/issues/9)

##  0.2.8

### added

- update readme
- Added some more configuration options for log and debug messages when running tests in the debug console
- debug console now shows source and line number from log messages
- use of debugpy from vscode Python extension, no separate installation of debugpy required
- implement test tags in test controller
- implement completion, hover and goto for variables

##  0.2.7

### added

- update readme
- add run and debug menus to editor title and context menu

##  0.2.6

### added

- update readme
- semantic tokens now iterate over nodes

##  0.2.5

### added

- correct loading and closing documents/library/resources
- correct casefold in completion of namespaces

##  0.2.4

### added

- improve performance
- implement semantic syntax highlightning

##  0.2.2

### added

- integrate robotframework-tidy for formatting

## 0.2.1

### added

- improve test run messages
- add "Taks" to section completion
- add colors to test output

## 0.2.0

- Initial release


---

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.
