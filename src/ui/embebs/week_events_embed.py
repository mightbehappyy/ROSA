import discord

from src.apis.services.calendar_service import CalendarService
from src.utils.functions.translate_day import translate


class WeekEventsEmbed:
    def __init__(self, lab, lab_name):
        self.calendar_service = CalendarService(lab)
        self.lab = lab
        self.lab_name = lab_name

    def get_week_events_embed(self):
        date_range = self.calendar_service.get_calendar_week_range()
        events_by_day = self.calendar_service.get_calendar_events()
        embed = discord.Embed(
            title=f"Reservas do Laboratório {self.lab_name}",
            description=f"Horário da semana para as reservas dos laboratórios \n `{date_range}`",
            color=0xF03A17,
        )

        for day, events in events_by_day.items():
            day_events = "\n".join(
                f"Reserva para: {event['summary']} \nHorário: {event['start']} às {event['end']}\n"
                for event in events
            )

            embed.add_field(
                name=f"{translate(day)}",
                value=f"```{day_events}```",
                inline=False,
            )

        if not events_by_day:
            embed.add_field(
                name="Nenhum evento encontrado",
                value="Não há horários reservados para essa semana",
                inline=False,
            )

        return embed
