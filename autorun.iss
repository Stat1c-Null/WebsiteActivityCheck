; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{4F0AFCC0-A8ED-4F9F-90E0-E0A25B80617D}
AppName=Website Activity Checker
AppVersion=-1
;AppVerName=Website Activity Checker -1
AppPublisher=Nickitos Incorporated
AppPublisherURL=https://www.example.com/
AppSupportURL=https://www.example.com/
AppUpdatesURL=https://www.example.com/
DefaultDirName={autopf}\Website Activity Checker
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\_Projects\Nick\AppWithNoIcon
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "czech"; MessagesFile: "compiler:Languages\Czech.isl"
Name: "hebrew"; MessagesFile: "compiler:Languages\Hebrew.isl"
Name: "icelandic"; MessagesFile: "compiler:Languages\Icelandic.isl"
Name: "polish"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "slovak"; MessagesFile: "compiler:Languages\Slovak.isl"
Name: "ukrainian"; MessagesFile: "compiler:Languages\Ukrainian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\_Projects\Nick\WebsiteActivityCheck\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\_Projects\Nick\WebsiteActivityCheck\data.csv"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\_Projects\Nick\WebsiteActivityCheck\log.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\_Projects\Nick\WebsiteActivityCheck\new_data.csv"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\.myp\OpenWithProgids"; ValueType: string; ValueName: "WebsiteActivityCheckerFile.myp"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\WebsiteActivityCheckerFile.myp"; ValueType: string; ValueName: ""; ValueData: "Website Activity Checker File"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\WebsiteActivityCheckerFile.myp\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\main.exe,0"
Root: HKA; Subkey: "Software\Classes\WebsiteActivityCheckerFile.myp\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\main.exe"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\main.exe\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\Website Activity Checker"; Filename: "{app}\main.exe"
Name: "{autodesktop}\Website Activity Checker"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Website Activity Checker}"; Flags: nowait postinstall skipifsilent
