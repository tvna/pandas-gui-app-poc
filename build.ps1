Write-Output "Initialize C compling..."
Measure-Command {
    nuitka `
        --mingw64 `
        --plugin-enable=numpy `
        --plugin-enable=tk-inter `
        --plugin-enable=pkg-resources `
        --windows-product-name="pandas-nuitka-gui-poc" `
        --windows-company-name="TBA" `
        --windows-file-version="0.1.0.0" `
        --windows-file-description="this is pandas GUI PoC" `
        --windows-onefile-tempdir `
        --windows-disable-console `
        --standalone `
        --onefile `
        --show-progress `
        --output-dir=."\dist" `
        .\main.py 

        # other nuitka options
        # --windows-icon-from-ico=ICON_PATH
        # --include-data-file=favicon.ico
        # --include-data-dir=DATA_DIRS
}