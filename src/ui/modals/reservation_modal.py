import discord
import traceback
from datetime import datetime
from src.ui.embebs.confirmation_embed import ConfirmationEmbed

from src.apis.services.calendar_service import CalendarService
from src.utils.functions.date_time_validation import validate_date_time_format
from src.ui.embebs.day_events_embed import DayEventsEmbed

class ReservationModal(discord.ui.Modal, title="Reserva"):
    motivation = discord.ui.TextInput(
        label="Nome da Cadeira, Monitoria ou Curso",
        placeholder="Ex: Programação 2",
        required=True,
    )

    name = discord.ui.TextInput(
        label="Nome do autor da reserva", placeholder="Ex: Pedro Luiz", required=True
    )

    date = discord.ui.TextInput(
        label="Data da reserva",
        placeholder="Ex: 18-11-2023",
        required=True,
        max_length=10,
        min_length=10,
    )

    start_time = discord.ui.TextInput(
        label="Horário do início",
        placeholder="Ex: 09:10 ",
        required=True,
        max_length=5,
        min_length=5,
    )

    ending_time = discord.ui.TextInput(
        label="Horário do termino",
        placeholder="Ex: 12:30 ",
        required=True,
        max_length=5,
        min_length=5,
    )

    async def on_submit(self, interaction: discord.Interaction):
        calendar_service = CalendarService(1)
        motivation_value = self.motivation.value
        name_value = self.name.value
        date_value = self.date.value
        start_time_value = self.start_time.value
        ending_time_value = self.ending_time.value
        date_obj = datetime.strptime(date_value, "%d-%m-%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")

        validation_result = await validate_date_time_format(date_value, start_time_value, ending_time_value)

        if validation_result != "formato válido":
            await interaction.response.send_message(
                f"Formato inválido da {validation_result}",
                ephemeral=True,
            )

        try:
            event = calendar_service.post_calendar_event(
                motivation_value + "-" + name_value, start_time_value, ending_time_value, formatted_date)
            if event == 409:
                user = await interaction.client.fetch_user(interaction.user.id)

                day_events_embed = DayEventsEmbed(1)
                embed = day_events_embed.get_week_events_embed(date_value)
                await interaction.response.send_message(embed=embed, ephemeral=True)

            elif event == 400:
                await interaction.response.send_message(
                    "O formato da data/hora é -> Hora:Minuto e Dia-Mês-Ano",
                    ephemeral=True,
                )

            else:
                user = await interaction.client.fetch_user(interaction.user.id)
                await interaction.response.send_message(
                    f"<@{user.id}> Reserva enviada com sucesso! Veja a confirmação na sua DM :white_check_mark:"
                )
                embed_object = ConfirmationEmbed()
                print(event)
                embed = embed_object.send_confirmation_embed(
                    event["summary"],
                    event["start"],
                    event["end"],
                    event["date"],
                    name_value,
                )

                await user.send(embed=embed)

        except Exception as e:
            print("erro tal:", e)
            await interaction.response.send_message(
                "Ocorreu um erro ao enviar a reserva :cry:",
                ephemeral=True,
            )

    async def on_error(
            self, interaction: discord.Interaction, error: Exception
    ) -> None:
        await interaction.followup.send(
            "Eita! alguma coisa deu errado.", ephemeral=True
        )

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
