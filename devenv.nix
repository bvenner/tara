{ pkgs, lib, config, inputs, ... }:
{
  # Basic environment variables
  env.ANYTYPE_API_BASE_URL = "http://127.0.0.1:31012";

  # Enable dotenv integration
  dotenv.enable = true;

  # Python managed by uv (pyproject.toml + uv.lock are the single source of
  # truth; uv inputs provide a pinned CPython with the GLIBC/libstdc++ the
  # binary deps of docling need).
  languages.python.enable = true;
  languages.python.version = "3.13";
  languages.python.uv.enable = true;

  # Packages from nixpkgs (always available in shell)
  packages = [
    pkgs.sops
    pkgs.age
    pkgs.nodejs_22
    pkgs.jq
    pkgs.curl
    pkgs.git
    pkgs.gh
    pkgs.uv
    pkgs.zlib
    pkgs.stdenv.cc.cc.lib
  ];

  enterShell = ''
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║  TARA devenv loaded                                           ║"
    echo "╠═══════════════════════════════════════════════════════════════╣"
    echo "║  uv --version          # Python pinned via pyproject+uv.lock  ║"
    echo "║  node --version        # MCP server runtime                   ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Usage: uv sync   (provision .venv from the pinned lockfile)"
    echo "       uv run python ... (run a script in the managed venv)"
  '';
}