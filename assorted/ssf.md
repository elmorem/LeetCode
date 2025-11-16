why does my instance of cluely keep crashing? can yo investigate?
Here’s a fast path to diagnose and stabilize Cluely on macOS:

Update first: quit Cluely, then reinstall the latest build from Cluely, dated after Nov 16, 2025.
Verify permissions: System Settings > Privacy & Security > enable Cluely for Screen Recording, Microphone, Accessibility, Files and Folders.

Kill conflicting overlays: fully quit Zoom, Discord, Slack huddles, Notion widgets, NVIDIA/AMD screen tools.
Toggle hardware acceleration: in Cluely Settings > Performance, turn Hardware Acceleration off, relaunch. If already off, turn it on and relaunch.

Clear cache only: remove Cluely cache, keep sessions
rm -rf ~/Library/Caches/Cluely
rm -rf ~/Library/Application\ Support/Cluely/Cache
Reset TCC permissions if prompts are stuck
tccutil reset All com.cluely.app
Collect crash data for root cause
Open Console.app > Crash Reports > look for Cluely and note the Exception Type and crashed thread
Files live in ~/Library/Logs/DiagnosticReports/ with names like Cluely_*.crash
Runtime logs
log show --predicate 'process == "Cluely"' --last 2h > ~/Desktop/cluely-log.txt
Check GPU and Rosetta status
About This Mac > Chip; if Intel, ensure no Rosetta-only plugin is injected
If Apple Silicon and Cluely is running under Rosetta, launch the native build
Disable VS Code screen capture while testing since it is already using the screen APIs in your screenshot
Network sanity
Turn off VPN or corporate proxies temporarily
Ensure api.cluely domains are reachable with curl
One-command collector to bundle diagnostics on your Desktop:

mkdir -p ~/Desktop/cluely-diagnostics && \
cp ~/Library/Logs/DiagnosticReports/Cluely*.crash ~/Desktop/cluely-diagnostics 2>/dev/null || true && \
log show --predicate 'process == "Cluely"' --last 2h > ~/Desktop/cluely-diagnostics/runtime.log && \
system_profiler SPHardwareDataType SPDisplaysDataType > ~/Desktop/cluely-diagnostics/system.txt && \
echo "Done: ~/Desktop/cluely-diagnostics"
Most frequent culprits: missing Screen Recording permission, overlay conflicts from Zoom or Discord, GPU acceleration crashes on certain drivers, or stale cache after an update.