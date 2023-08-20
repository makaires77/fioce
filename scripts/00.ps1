# Pasta raiz do projeto
$projectRoot = "C:\Users\marco\fioce\"

# Lista de pastas a serem verificadas e criadas, se necessário
$foldersToCreate = @(
    "source\adapters\input\jupyter_notebooks",
    "source\adapters\output\models",
    "source\application\use_cases",
    "source\domain\entities",
    "source\domain\repositories",
    "source\infrastructure\data_sources",
    "tests\unit",
    "tests\integration"
)

# Verifica e cria as pastas
foreach ($folder in $foldersToCreate) {
    $fullPath = Join-Path -Path $projectRoot -ChildPath $folder

    if (!(Test-Path -Path $fullPath -PathType Container)) {
        Write-Host "Creating folder: $fullPath"
        New-Item -Path $fullPath -ItemType Directory -Force
    }
}

Write-Host "Folders checked and created (if necessary)."