{pkgs, ...}: {
  # Basic environment variables
  env.ANYTYPE_API_BASE_URL = "http://127.0.0.1:31012";

  # Enable dotenv integration
  dotenv.enable = true;

  # Packages from nixpkgs (always available in shell)
  packages = with pkgs; [
    anytype-cli
    sops
    age
    nodejs_22
    jq
    curl
    git
    gh
  ];

  enterShell = ''
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║  TARA devenv loaded                                           ║"
    echo "╠═══════════════════════════════════════════════════════════════╣"
    echo "║  anytype-cli --version # AnyType CLI (headless server)        ║"
    echo "║  node --version        # MCP server runtime                 ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Start AnyType headless server: anytype-cli serve"
    echo "API endpoint: http://127.0.0.1:31012"
  '';
}
