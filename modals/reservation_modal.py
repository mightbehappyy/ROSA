import discord
import traceback
from datetime import datetime
from apis.CalendarAPI import post_event
from embebs.confirmation_embed import ConfirmationEmbed
from embebs.reservation import ReservationEmbeds
from apis.CalendarAPI import get_day_event


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
        embed_object = ConfirmationEmbed()
        motivation_value = self.motivation.value
        name_value = self.name.value
        date_value = self.date.value
        start_time_value = self.start_time.value
        ending_time_value = self.ending_time.value
        try:
            date_obj = datetime.strptime(date_value, "%d-%m-%Y")
            formatted_date = date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            await interaction.response.send_message(
                "Formato de data inválido por favor use: Dia-Mês-Ano.", ephemeral=True
            )
            print(e)

        try:
            datetime.strptime(start_time_value, "%H:%M")
            datetime.strptime(ending_time_value, "%H:%M")
        except ValueError as e:
            await interaction.response.send_message(
                "Formato de hora inválido por favor use: Hora:Minuto.", ephemeral=True
            )

            print(e)
            return

        try:
            event = post_event(
                motivation_value, start_time_value, ending_time_value, formatted_date
            )

            if event == True:
                embed = ReservationEmbeds()
                result_days_embed = embed.get_day_events_embed(
                    get_day_event(formatted_date)
                )

                await interaction.response.send_message(
                    ephemeral=True, embed=result_days_embed
                )

                return
            elif event == False:
                user = await interaction.client.fetch_user(interaction.user.id)
                await interaction.response.send_message(
                    f"<@{user.id}> Reserva enviada com sucesso! Veja a confirmação na sua DM :white_check_mark:"
                )
                embed = embed_object.send_confirmation_embed(
                    motivation_value,
                    start_time_value,
                    ending_time_value,
                    formatted_date,
                    name_value,
                )
                await user.send(embed=embed)
            else:
                await interaction.response.send_message(
                    "Ocorreu um erro ao enviar a reserva :cry:",
                    ephemeral=True,
                )
                return
        except Exception as e:
            await interaction.response.send_message(
                "Ocorreu um erro ao enviar a reserva :cry:",
                ephemeral=True,
            )

    async def on_error(
        self, interaction: discord.Interaction, error: Exception
    ) -> None:
        await interaction.response.send_message(
            "Eita! alguma coisa deu errado.", ephemeral=True
        )

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
