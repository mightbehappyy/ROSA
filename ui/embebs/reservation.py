import discord


class ReservationEmbeds:
    def translate_day(self, day):
        dict_days = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo",
        }
        for key, value in dict_days.items():
            if key == day:
                return value

    def get_day_events(self, day_events):
        event_strings = []
        for event in day_events:
            scheduled_time = (
                f'{event.get("start_hour", "")} - {event.get("end_hour", "")}'
            )
            summary = event.get("summary", "")
            event_strings.append(
                f"\nReserva para: {summary}\nHorário: {scheduled_time}"
            )
            event_strings.append("\n")

        return " ".join(event_strings)

    def get_week_events_embed(self, events_by_day, lab):
        if events_by_day:
            first_day_list_converted = list(events_by_day.items())[0][1]
            final_day_list_converted = list(events_by_day.items())[-1][1]

            first_day = list(first_day_list_converted.items())[0][0]
            final_day = list(final_day_list_converted.items())[0][0]

            date_range = f"De {first_day} a {final_day}"
            embed = discord.Embed(
                title=f"Reservas do Laboratório {'Windows' if lab == 1 else 'Linux'}",
                description=f"Horário da semana para as reservas dos laboratórios ({date_range})",
                color=0xF03A17,
            )

            for day_name, day_data in events_by_day.items():
                dates = list(day_data.keys())

                day = self.translate_day(day_name)

                embed.add_field(
                    name=f"{(day)}",
                    value=f"```{self.get_day_events(day_data[dates[0]])}```"
                    if dates
                    else "No events",
                    inline=False,
                )
            embed.add_field(name="", value="", inline=True)

            return embed
        else:
            return discord.Embed(
                title="Não há horários reservados para essa semana",
                color=0xF03A17,
            )

    def get_day_events_embed(self, events):
        if events:
            first_day_list_converted = list(events.items())[0][1]

            first_day = list(first_day_list_converted.items())[0][0]

            embed = discord.Embed(
                title="Infelizmente já existe existe uma reserva para esse horário :cry:",
                description=f"Aqui estão as reservas para {first_day} tente reservar para outro horário se possível :smiley:",
                color=0xF03A17,
            )

            for day_name, day_data in events.items():
                dates = list(day_data.keys())

                day = self.translate_day(day_name)

                embed.add_field(
                    name=f"{(day)}",
                    value=f"```{self.get_day_events(day_data[dates[0]])}```"
                    if dates
                    else "No events",
                    inline=False,
                )
            embed.add_field(name="", value="", inline=True)

            return embed
