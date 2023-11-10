from yoklama.base import Module


class DonanimHaber(Module):
    name = "donanimhaber.com"
    url = "https://search.donanimhaber.com/api/autocomplete/member/?token=-1"

    async def check(self) -> bool:
        value = self.get_value()
        response = await self.client.post(self.url, content=value)
        if not response.is_success:
            return False

        data = response.json()
        members = data.get("members")
        if not members:
            return False

        try:
            member = next(
                member
                for member in members
                if member.get("login", "").casefold() == value.casefold()
            )
        except StopIteration:
            return False

        member_id = member["id"]
        self.response_url = f"https://forum.donanimhaber.com/profil/{member_id}"
        return True

    def get_value(self) -> str:
        return self.value.strip()
