[Setup]
AppName=Fat Llama Desktop
AppVersion=1.0
DefaultDirName={pf}\FatLlamaDesktop
DefaultGroupName=Fat Llama Desktop
OutputBaseFilename=fat_llama_windows_installer
OutputDir=installers/windows
Compression=lzma
SolidCompression=yes
SetupIconFile=fat_llama_desktop\assets\logo.ico
UninstallDisplayIcon={app}\assets\logo.ico
UninstallFilesDir={app}
UninstallDisplayName=Fat Llama Desktop

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: checkedonce
Name: "startmenuicon"; Description: "Create a &Start Menu icon"; GroupDescription: "Additional icons:"; Flags: checkedonce

[Files]
Source: "dist\FatLlamaDesktop\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
Filename: "{app}\FatLlamaDesktop.exe"; Parameters: ""; WorkingDir: "{app}"; Flags: nowait postinstall

[Icons]
Name: "{group}\Fat Llama Desktop"; Filename: "{app}\FatLlamaDesktop.exe"; IconFilename: "{app}\assets\logo.ico"
Name: "{group}\Uninstall Fat Llama Desktop"; Filename: "{app}\unins000.exe"
Name: "{autodesktop}\Fat Llama Desktop"; Filename: "{app}\FatLlamaDesktop.exe"; IconFilename: "{app}\assets\logo.ico"; Tasks: desktopicon
Name: "{userstartmenu}\Programs\Fat Llama Desktop"; Filename: "{app}\FatLlamaDesktop.exe"; IconFilename: "{app}\assets\logo.ico"; Tasks: startmenuicon

[UninstallDelete]
Type: files; Name: "{app}\*"

[Code]
function IsPythonInstalled: Boolean;
var
  ResultCode: Integer;
begin
  Exec('cmd', '/c python --version', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  Result := ResultCode = 0;
  if not Result then begin
    MsgBox('Python is not installed. Please install Python 3.9 or later.', mbError, MB_OK);
  end;
end;

function IsFFmpegInstalled: Boolean;
var
  ResultCode: Integer;
begin
  Exec('cmd', '/c ffmpeg -version', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  Result := ResultCode = 0;
  if not Result then begin
    MsgBox('FFmpeg is not installed. Please install FFmpeg.', mbError, MB_OK);
  end;
end;

function InitializeSetup: Boolean;
begin
  Result := IsPythonInstalled and IsFFmpegInstalled;
end;
