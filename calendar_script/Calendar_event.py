import pytz
from datetime import datetime


'''
{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 25 - 27, Mon to Wed, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-25T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-26T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 25 - 27, Mon to Wed, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-26T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-27T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nFor Brooklyn stations, take the [R] or use nearby Borough Hall [2][4].\n\nFor Manhattan, take the [R] for Whitehall St-South Ferry or use nearby [4] or [J] stations.\n\nTransfer at:\nAtlantic Av [N][R][2][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nNote: At Canal St, uptown [N] trains stop at the [Q] platform during this time.\nNov 25 - 27, Mon to Wed, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-25T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-26T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nFor Brooklyn stations, take the [R] or use nearby Borough Hall [2][4].\n\nFor Manhattan, take the [R] for Whitehall St-South Ferry or use nearby [4] or [J] stations.\n\nTransfer at:\nAtlantic Av [N][R][2][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nNote: At Canal St, uptown [N] trains stop at the [Q] platform during this time.\nNov 25 - 27, Mon to Wed, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-26T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-27T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, [N] runs local in both directions between DeKalb Av and 59 St\nSchedule reminder: Late night [N] also runs local between these stations.\nNov 23 - 24, Sat and Sun, 5:45 AM to 11:30 PM', 'colorId': '2', 'start': {'dateTime': '2024-11-23T05:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-23T23:30:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, [N] runs local in both directions between DeKalb Av and 59 St\nSchedule reminder: Late night [N] also runs local between these stations.\nNov 23 - 24, Sat and Sun, 5:45 AM to 11:30 PM', 'colorId': '2', 'start': {'dateTime': '2024-11-24T05:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-24T23:30:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St, 28 St and 49 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq, 34 St-Herald Sq or 57 St-7 Av and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to Times Sq-42 St, 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 18 - 21, Mon to Thu, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-18T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-19T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St, 28 St and 49 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq, 34 St-Herald Sq or 57 St-7 Av and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to Times Sq-42 St, 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 18 - 21, Mon to Thu, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-19T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-20T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St, 28 St and 49 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq, 34 St-Herald Sq or 57 St-7 Av and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to Times Sq-42 St, 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 18 - 21, Mon to Thu, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-20T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-21T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tip:\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] to DeKalb Av\nNov 18 - 21, Mon to Thu, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-18T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-19T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tip:\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] to DeKalb Av\nNov 18 - 21, Mon to Thu, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-19T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-20T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tip:\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] to DeKalb Av\nNov 18 - 21, Mon to Thu, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-20T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-21T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Lower Manhattan and Brooklyn, Coney Island-bound [N] local runs via the [Q] from Canal St to DeKalb Av\nIn Manhattan, use nearby [4] or [J] stations for City Hall, Cortlandt St, Rector St and Whitehall St-South Ferry.\n\nIn Brooklyn, use nearby Borough Hall [2][4] for Court St and Jay St-MetroTech.\n\nTransfer at:\n14 St-Union Sq [N][4]\nCanal St [N] [J] ([4] after 1 AM)\nAtlantic Av [N][2][4]\nTravel tip:\nFor service to Court St and Jay St-MetroTech, take the [N] to DeKalb Av\nNov 21 - 22, Thu 11:45 PM to Fri 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-21T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-22T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [2][4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][R][2][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tips:\nFor service to Jay St-MetroTech, Court St and Whitehall St-South Ferry, take the [R] via transfer at Atlantic Av-Barclays Ctr.\n\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] or Bay Ridge-bound [R] to DeKalb Av\nNov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-11T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-12T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [2][4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][R][2][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tips:\nFor service to Jay St-MetroTech, Court St and Whitehall St-South Ferry, take the [R] via transfer at Atlantic Av-Barclays Ctr.\n\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] or Bay Ridge-bound [R] to DeKalb Av\nNov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-12T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-13T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [2][4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][R][2][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tips:\nFor service to Jay St-MetroTech, Court St and Whitehall St-South Ferry, take the [R] via transfer at Atlantic Av-Barclays Ctr.\n\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] or Bay Ridge-bound [R] to DeKalb Av\nNov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-13T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-14T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn and Lower Manhattan, Astoria-bound [N] local runs via the [Q] from DeKalb Av to Canal St\nIn Brooklyn, use nearby Borough Hall [2][4] for Jay St-MetroTech and Court St.\n\nIn Manhattan, use nearby [4] or [J] stations for Whitehall St-South Ferry, Rector St, Cortlandt St and City Hall.\n\nTransfer at:\nAtlantic Av [N][R][2][4]\nCanal St [N][J] ([4] after 1:30 AM)\n14 St-Union Sq [N][4]\nTravel tips:\nFor service to Jay St-MetroTech, Court St and Whitehall St-South Ferry, take the [R] via transfer at Atlantic Av-Barclays Ctr.\n\nFor service from Court St and Jay St-MetroTech, take a Coney Island-bound [N] or Bay Ridge-bound [R] to DeKalb Av\nNov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-14T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-15T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, no [N] at Coney Island-Stillwell Av\n[N] runs between Astoria-Ditmars Blvd and 86 St, the last stop.\n\nFree shuttle buses run between 86 St and Coney Island-Stillwell Av.\n\nFor service between Manhattan and Coney Island-Stillwell Av, take the [D][F] or [Q] instead.\n\nTransfer stations:\n34 St-Herald Sq\nNov 9 - 10, Sat 3:45 AM to Sun 10:00 PM', 'colorId': '2', 'start': {'dateTime': '2024-11-09T03:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-10T22:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-04T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-05T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-05T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-06T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-06T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-07T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-07T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-08T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-11T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-12T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-12T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-13T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-13T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-14T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, Manhattan-bound [N] local skips 53 St, 45 St, 25 St, Prospect Av, 4 Av-9 St and Union St\nFor service to 53 St and 45 St, take the [N] to 36 St and transfer to a Coney Island-bound [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [N] or [R] to 59 St and transfer to a Manhattan-bound [N].\n\nFor service to 25 St, Prospect Av, 4 Av-9 St and Union St, take the [N] to Atlantic Av-Barclays Ctr and transfer to a local Coney Island-bound [D] [N] or Bay Ridge-bound [R].\n\nFor service from these stations, take the [D][N] or [R] to 36 St and transfer to a Manhattan-bound [N].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-14T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-15T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Brooklyn, no [N] at Coney Island-Stillwell Av\n[N] runs between Astoria-Ditmars Blvd and 86 St, the last stop.\n\nFree shuttle buses run between 86 St and Coney Island-Stillwell Av.\n\nFor service between Manhattan and Coney Island-Stillwell Av, take the [D][F] or [Q] instead.\n\nTransfer stations:\n34 St-Herald Sq\nNov 5, Tuesday, 9:45 AM to 3:00 PM', 'colorId': '2', 'start': {'dateTime': '2024-11-05T09:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-05T15:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-04T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-05T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-05T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-06T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-06T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-07T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-07T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-08T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-11T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-12T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-12T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-13T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-13T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-14T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

{'summary': 'N planned work', 'description': 'In Manhattan, uptown [N][Q] skips Prince St, 8 St-NYU, 23 St and 28 St\nFor service to these stations, take the [N] or [Q] to 14 St-Union Sq or 34 St-Herald Sq and transfer to a downtown train.\n\nFor service from these stations, take a downtown train to 14 St-Union Sq or Canal St and transfer to an uptown [N] or [Q].\nNov 4 - 8 and Nov 11 - 15, Mon to Fri, 11:45 PM to 5:00 AM', 'colorId': '2', 'start': {'dateTime': '2024-11-14T23:45:00-05:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2024-11-15T05:00:00-05:00', 'timeZone': 'America/New_York'}} 

'''

consolidated_active_periods = {}

class Calendar_event:
    def __init__(self, service, calendar_id, notificiation_type, alert_id, train_id, active_periods, header_text, description_text, updated_at, human_readable_active_period):
        
        self.service = service
        self.calendar_id = calendar_id
        self.notificiation_type = notificiation_type
        self.alert_id = alert_id
        self.train_id = train_id
        self.header_text = header_text
        self.description = description_text
        self.updated_at = updated_at
        self.human_readable_active_period = human_readable_active_period
        self.active_periods = active_periods
        self.event = self.initialize_event()

    def color_code_event(self):
        if self.notificiation_type == 'alert':
            return '3'
        
        return '3'
    
    def get_active_periods(self):
        return self.active_periods

    def initialize_event(self):
        self.event = {
            'summary': f'{self.train_id} {self.notificiation_type}',
            'description': self.header_text + '\n' + self.description + '\n' + 'Complete schedule:' + '\n' + self.human_readable_active_period,
            'colorId': self.color_code_event(), 
            'start': {
                'dateTime': '',
                'timeZone': 'America/New_York'
            },
            'end': {
                'dateTime': '',
                'timeZone': 'America/New_York'
            }
        }

        return self.event
    

    def format_rfc3339(self, timestamp):
        dt = datetime.fromtimestamp(timestamp, pytz.timezone('America/New_York'))
        return dt.isoformat()
    

    def post_events(self, service):

        
        for i in range(len(self.active_periods)):

            # print(f'Start: {self.active_periods[i][0]}. End: {self.active_periods[i][1]}')
            
            start = self.format_rfc3339(self.active_periods[i][0])
            end = self.format_rfc3339(self.active_periods[i][1])

            self.event['start']['dateTime'] = start
            self.event['end']['dateTime'] = end
            
            
            time_key = f'{self.active_periods[i][0]}{self.active_periods[i][1]}'

            # print(f'Time key: {time_key}')

            if time_key not in consolidated_active_periods:
                # print('New time key')
                mark_event = service.events().insert(calendarId=self.calendar_id, body=self.event).execute()
                event_id = mark_event.get('id')
                consolidated_active_periods[time_key] = event_id
            else:
                
                occupying_event_id = consolidated_active_periods[time_key] 
                # print(f'Existing time key: {occupying_event_id}')


                occupying_event = service.events().get(calendarId=self.calendar_id, eventId=occupying_event_id).execute()

                # print(f'Old event: {occupying_event['description']}')
                occupying_event['description'] = occupying_event['description'] + '\n\nNEXT ALERT: \n' + self.event.get('description')
                # print(f'\nNew event: {occupying_event['description']}')

                service.events().update(calendarId=self.calendar_id, eventId=occupying_event_id, body=occupying_event).execute()




        


            # print(self.event, "\n")

            # executed_event = 

            

    
        
        return 0









