import re
import requests

def check_vac_status(steam_id):
    url = f"https://steamcommunity.com/profiles/{steam_id}"

    try:
        response = requests.get(url)
        html_content = response.text

        # 使用正则表达式查找VAC信息
        vac_pattern = r'<div class="profile_ban_status">(.+?)<\/div>'
        vac_match = re.search(vac_pattern, html_content, re.DOTALL)

        if vac_match:
            vac_status = vac_match.group(1).strip()
            if "VAC banned" in vac_status:
                print(f"The user with Steam ID {steam_id} is VAC banned.")
            else:
                print(f"The user with Steam ID {steam_id} is not VAC banned.")
        else:
            print(f"Could not find VAC status information for Steam ID {steam_id}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# 示例用法
if __name__ == "__main__":
    steam_id_to_check = 'id'  # 替换为你要查询的Steam账号的Steam ID
    check_vac_status(steam_id_to_check)