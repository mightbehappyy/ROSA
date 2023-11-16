import discord


def check_for_role(interaction: discord.Interaction, authorized_role: int):
    for role in interaction.user.roles:
        print(role.id == authorized_role)
        if role.id == authorized_role:
            return True
    return False
