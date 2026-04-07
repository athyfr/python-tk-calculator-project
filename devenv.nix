{
  pkgs,
  ...
}:

{
  packages = [ pkgs.git ];

  languages.python = {
    enable = true;
    package = pkgs.python314.withPackages (ps: [ ps.tkinter ]);
    venv.enable = true;
    venv.requirements = ./requirements.txt;
  };
}
