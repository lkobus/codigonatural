using System;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;

namespace DiscordBotShuffler
{
    class Program
    {
        private static DiscordSocketClient _client;
        private static ulong _channelId = Variables.CHANNEL_ID; // Substitua pelo ID do canal que você deseja enviar mensagens

        static async Task Main(string[] args)
        {
            _client = new DiscordSocketClient();

            _client.Log += LogAsync;
            _client.Ready += ReadyAsync;

            // Token do seu bot do Discord
            string token = Variables.BOT_TOKEN;
            
            // Inicializa o bot
            await _client.LoginAsync(TokenType.Bot, token);
            await _client.StartAsync();

            // Inicializa o servidor HTTP
            var host = new WebHostBuilder()
                .UseKestrel()
                .Configure(app =>
                {
                    app.Run(HandleRequestAsync);
                })
                .Build();

            await host.RunAsync();

            await Task.Delay(-1);
        }

        private static async Task HandleRequestAsync(HttpContext context)
        {            
            if (context.Request.Path == "/enviar-mensagem")
            {
                // Verifica se o parâmetro 'texto' está presente na query string
                if(context.Request.Query.ContainsKey("texto"))
                {
                    string mensagem = context.Request.Query["texto"];

                    var guild = _client.GetGuild(Variables.SERVER_ID); // Substitua pelo ID do seu servidor
                    var channel = guild.GetTextChannel(_channelId);

                    await channel.SendMessageAsync(mensagem);

                    await context.Response.WriteAsync($"Mensagem '{mensagem}' enviada com sucesso!");
                }
                else
                {
                    await context.Response.WriteAsync("Parâmetro 'texto' não encontrado na URL.");
                }
            }
            else
            {
                context.Response.StatusCode = 404;
                await context.Response.WriteAsync("Endpoint não encontrado.");
            }
        }


        private static Task LogAsync(LogMessage log)
        {
            Console.WriteLine(log.ToString());
            return Task.CompletedTask;
        }

        private static async Task ReadyAsync()
        {
            Console.WriteLine($"Logged in as {_client.CurrentUser}");
        }
    }
}
