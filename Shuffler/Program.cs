using System;
using System.Diagnostics;
static void PlayAudio(string filePath)
{
    try
    {
        // Comando PowerShell para reproduzir o arquivo de áudio
        string powerShellCommand = $"-c \"& {{ [System.Media.SoundPlayer]::new('{filePath}').PlaySync(); }}\"";

        // Configurar o processo para invocar o PowerShell
        ProcessStartInfo processInfo = new ProcessStartInfo
        {
            FileName = "powershell.exe",
            Arguments = powerShellCommand,
            CreateNoWindow = true,   // Não exibir janela do PowerShell
            UseShellExecute = false, // Não usar o shell padrão
            RedirectStandardOutput = true,
            RedirectStandardError = true
        };

        // Criar e iniciar o processo
        using (Process process = new Process())
        {
            process.StartInfo = processInfo;
            process.Start();

            // Aguardar até que o processo termine
            process.WaitForExit();

            // Verificar se ocorreram erros durante a execução
            if (process.ExitCode != 0)
            {
                string errorMessage = process.StandardError.ReadToEnd();
                Console.WriteLine($"Erro ao executar PowerShell: {errorMessage}");
            }
            else
            {
                Console.WriteLine($"Áudio reproduzido: {filePath}");
            }
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Ocorreu um erro ao reproduzir o áudio: {ex.Message}");
    }
}
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

string stagesFolder = @"E:\shuffle_overlay\stages\";
string selectedStagePath = @"E:\shuffle_overlay\selected-stage.png";
string shuffle_label = @"E:\shuffle_overlay\shuffler_label.txt";

File.WriteAllText(shuffle_label, "Sorteando mapa");
// Deletar o arquivo selected-stage.png se ele existir
if (File.Exists(selectedStagePath))
{
    File.Delete(selectedStagePath);
}

// Esperar 3 segundos

Thread.Sleep(3000);

// Lista de estágios
string[] stages = {
    "Akademia Fountain Courtyard",
    "Alexandria",
    "Besaid",
    "Cornelia",
    "Eden",
    "Floating Continent",
    "Insomnia",
    "Interdimensional Rift",
    "Midgar",
    "Moon",
    "Narsche",
    "Orbone Monastery",
    "Padaemonium",
    "Porta Decumana",
    "Rabanastre",
    "Stella Fulcrum",
    "The Final Battlefield",
    "The Promised Meadow"
};

// Escolher um estágio aleatoriamente
Random random = new Random();
int randomIndex = random.Next(0, stages.Length);
string selectedStage = stages[randomIndex];

// Copiar o arquivo do estágio selecionado para selected-stage.png
string stageFilePath = Path.Combine(stagesFolder, $"{selectedStage}.png");
if (File.Exists(stageFilePath))
{
    
    File.Copy(stageFilePath, selectedStagePath);
    File.WriteAllText(shuffle_label, selectedStage);            
    Thread.Sleep(500);
    PlayAudio(@"E:\shuffle_overlay\audios\movement-swipe-whoosh-2-186576.wav");
    Console.WriteLine($"Estágio '{selectedStage}' selecionado e copiado para {selectedStagePath}");
}
else
{
    Console.WriteLine($"Arquivo do estágio '{selectedStage}' não encontrado em {stageFilePath}");
}
