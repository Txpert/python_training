
### Manuelles Backup

1. **Einstellungen-Dateien finden:**
   - **Benutzereinstellungen**: Diese befinden sich in der `settings.json` Datei.
     - Auf Windows: `C:\Users\<Dein Benutzername>\AppData\Roaming\Code\User\settings.json`
     - Auf macOS: `~/Library/Application Support/Code/User/settings.json`
     - Auf Linux: `~/.config/Code/User/settings.json`
   - **Workspaces-Einstellungen**: Diese befinden sich im `.vscode` Ordner innerhalb deines Projektverzeichnisses.

2. **Einstellungen-Dateien kopieren:**
   - Kopiere einfach die `settings.json` Datei (und andere relevante Dateien wie `keybindings.json`, `snippets`, etc.) an einen Sicherungsort.

### Einstellungen exportieren mit Erweiterungen


1. **Integrierte Settings Sync-Funktion (VS Code 1.48+):**
   - Öffne die Befehlspalette (`Ctrl + Shift + P`).
   - Tippe `Settings Sync: Turn On`.
   - Folge den Anweisungen, um dich mit deinem Microsoft- oder GitHub-Konto anzumelden.
   - Dies synchronisiert deine Einstellungen, Tastenkombinationen, Erweiterungen und mehr auf verschiedenen Geräten.

### Einstellungen exportieren mit der Kommandozeile

1. **Einstellungen exportieren:**
   - Öffne das Terminal in VS Code.
   - Verwende den Befehl, um die Einstellungsdatei an einen anderen Ort zu kopieren:
     ```sh
     cp ~/.config/Code/User/settings.json ~/Schreibtisch/settings.json
     ```

2. **Einstellungen importieren:**
   - Verwende ähnlich den Befehl, um die Einstellungsdatei aus deinem Backup wiederherzustellen:
     ```sh
     cp ~/backup/settings.json ~/.config/Code/User/settings.json
     ```



Ctrl+P      : brings up the command palette
Ctrl+F      : find text on the page
Ctrl+Shift+O : list every symbol in the code
Ctrl+Shift+P : brings up the command palette to run commands
Ctrl+G      : go to a specific line number
Ctrl+D      : select the next occurrence of the selected word
fn+Click   : set up cursors in multiple places for multi-line editing
Ctrl+X      : cut the current line
alt+Up/Down : move the current line up or down
fn+Shift+Up/Down : copy the current line and move it up or down
Ctrl+/      : toggle comments on the selected code
Ctrl+Backtick : open a new terminal session in VS Code
Ctrl+K      : clear the terminal
Up Arrow    : go to the last command in the terminal history
Ctrl+Arrow  : navigate through text in the terminal
Ctrl+L      : highlight the current line
Ctrl+Shift+A : rename the symbol across all files
Ctrl+Shift+Period : list all symbols in the current file
Ctrl+Shift+B : run a task