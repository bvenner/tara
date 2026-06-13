{ pkgs, lib, config, inputs, ... }:

let
  anytype-cli = pkgs.stdenv.mkDerivation rec {
    pname = "anytype-cli";
    version = "0.3.2";

    src = pkgs.fetchurl {
      url = "https://github.com/anyproto/anytype-cli/releases/download/v${version}/anytype-cli-v${version}-linux-amd64.tar.gz";
      hash = "sha256-InauiWT7AWFuG3pLXZFmWybuEq4a8Aa8Uprtf5TIHpA=";
    };

    nativeBuildInputs = [ pkgs.autoPatchelfHook ];

    buildInputs = [
      pkgs.glibc
    ];

    sourceRoot = ".";

    installPhase = ''
      runHook preInstall
      mkdir -p $out/bin
      cp anytype $out/bin/
      chmod +x $out/bin/anytype
      runHook postInstall
    '';

    meta = with lib; {
      description = "AnyType CLI — headless AnyType server with embedded anytype-heart";
      homepage = "https://github.com/anyproto/anytype-cli";
      license = licenses.mit;
      platforms = [ "x86_64-linux" ];
      mainProgram = "anytype";
    };
  };
in
{
  # Basic environment variables
  env.ANYTYPE_CLI_VERSION = "0.3.2";
  env.ANYTYPE_API_BASE_URL = "http://127.0.0.1:31012";

  # Enable dotenv integration
  dotenv.enable = true;

  # Packages from nixpkgs (always available in shell)
  packages = [
    anytype-cli
    pkgs.sops
    pkgs.age
    pkgs.nodejs_22
    pkgs.jq
    pkgs.curl
    pkgs.git
    pkgs.gh
    pkgs.zlib
    pkgs.stdenv.cc.cc.lib
    pkgs.xorg.libxcb
    pkgs.xorg.libX11
    pkgs.xorg.libXext
    pkgs.xorg.libXrender
    pkgs.xorg.libXtst
    pkgs.xorg.libXi
    pkgs.glib
    pkgs.libGL
    pkgs.libglvnd
    pkgs.mesa
  ];

  # Python virtual environment (venv) for PyPI packages not in nixpkgs
  languages.python.enable = true;
  languages.python.venv.enable = true;

  # Ensure PyPI packages are installed into the devenv-managed venv on entry
  enterShell = ''
    VENV_PATH="$DEVENV_ROOT/.devenv/state/venv"
    REQUIREMENTS="$DEVENV_ROOT/requirements.txt"

    if [ -f "$REQUIREMENTS" ]; then
      echo "Ensuring PyPI packages from requirements.txt are installed..."
      "$VENV_PATH/bin/pip" install -q -r "$REQUIREMENTS"
    fi

    echo ""
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║  TARA devenv loaded                                           ║"
    echo "╠═══════════════════════════════════════════════════════════════╣"
    echo "║  anytype --version     # AnyType CLI (headless server)        ║"
    echo "║  python -c 'import docling'  # PDF extraction                 ║"
    echo "║  node --version        # MCP server runtime                 ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Start AnyType headless server: anytype serve"
    echo "API endpoint: http://127.0.0.1:31012"
  '';
}
