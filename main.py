from flet import *


def main(page: Page):
    page.title = "ECCAT"
    # page.window.height = 780
    # page.window.width = 400
    # page.window.top = 10
    # page.window.left = 960
    page.bgcolor = colors.WHITE
    page.theme_mode = ThemeMode.LIGHT

    def Intelligent_Terminal(w):
        page.launch_url(
            "https://drive.google.com/drive/folders/1Q1FhVyl1qEw7C5ZE-CRirT1XoHPxx3e9?usp=sharing")

    def Projects_Management(q):
        page.launch_url(
            "https://drive.google.com/drive/folders/1QLKSLDC7Q2Dt2HvsFr0hC5lNLgxgwXh2?usp=sharing")

    def Comprehensive_Mobile(e):
        page.launch_url(
            "https://drive.google.com/drive/folders/1n1mm9LZGAHh3Skhp_sKx_ijfKVmHETE6?usp=sharing")

    def Mobile_Network1(a):
        page.launch_url(
            "https://drive.google.com/drive/folders/1usMcvV-s5HZkHM_UzdrqtNp18f6wlsr_?usp=sharing")

    def Mobile_Network2(b):
        page.launch_url(
            "https://youtube.com/playlist?list=PLkFFXVGi-E56oLHouyI_W_geHok2Uep_H&si=z_opeJdDKwjAI5S_")

    def route_change(route):
        page.views.clear()
############# Home page ##########
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title=Text("ECCAT", font_family="lemonada"),
                        color="white",
                        bgcolor="black",
                    ),
                    Row([
                        Image(src="character_student.gif",
                              width=300, height=300,)
                    ], alignment=MainAxisAlignment("center")),
                    Text("Welcome To ECCAT", size=30, color="black",),
                    Text(""),
                    TextField(label="Username", color="BLUE_500"),
                    TextField(label="ID", color="BLUE_500"),
                    Text(""),
                    Row([
                        ElevatedButton("Continue", bgcolor=colors.BLUE_500, color="white", width=200, height=70, on_click=lambda _: page.go(
                            "/dep")),  # Bottun click to next page
                    ], alignment=MainAxisAlignment.CENTER),


                ]
            )
        )
#################################
########### departments page ###########
        if page.route == "/dep":
            page.views.append(
                View(
                    "/dep",
                    [
                        AppBar(
                            title=Text("Departments", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Department", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton("Communication", color="white", bgcolor=colors.BLUE_500,
                                       width=400, height=100, on_click=lambda _: page.go("/sem")),
                        ElevatedButton(
                            "Mechatronics", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/sem2")),
                        ElevatedButton(
                            "Electronics", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/sem3")),


                    ]
                )
            )
##################################
########### Comm grade ###########
        if page.route == "/comm":
            page.views.append(
                View(

                    "/comm",
                    [
                        AppBar(
                            title=Text("Communication",
                                       font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Your Grade", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton("First Grade", color="white", bgcolor=colors.BLUE_500,
                                       width=400, height=100),
                        ElevatedButton(
                            "Second Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                        ElevatedButton(
                            "Third Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                        ElevatedButton(
                            "Fourth Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/comm1")),
                    ]
                )
            )
##############
        ###### Comm subjects Page ######
        if page.route == "/comm1":
            page.views.append(
                View(

                    "/comm1",
                    [
                        AppBar(
                            title=Text("Subjects",
                                       font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Subject", width=350,
                             size=40, text_align="center"),
                        ElevatedButton("Intelligent Terminal Development Technology", color="white",
                                       bgcolor=colors.BLUE_500, width=400, height=100, on_click=Intelligent_Terminal),
                        ElevatedButton(
                            "Project Management", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=Projects_Management),
                        ElevatedButton(
                            "Mobile Network Testing and Optimization  ", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/mob")),
                        ElevatedButton(
                            "Comprehensive Mobile Network Optimization  ", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=Comprehensive_Mobile),
                    ]
                )
            )
        ########### mobile course #######
        if page.route == "/mob":
            page.views.append(
                View(
                    "/mob",
                    [
                        AppBar(
                            title=Text(
                                "Mobile Network", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Source", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton(
                            "Course Lectures", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=Mobile_Network1),
                        ElevatedButton(
                            "Course Videos", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=Mobile_Network2),


                    ]
                )
            )
            #################

        #######################
        # comm sem
        if page.route == "/sem":
            page.views.append(
                View(
                    "/sem",
                    [
                        AppBar(
                            title=Text(
                                "Semesters", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Semester", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton(
                            "First Semester", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/comm")),
                        ElevatedButton(
                            "Second Semester", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/comm2")),


                    ]
                )
            )
        #######################
########### second semester ########

        #### mecha Grade ###
        if page.route == "/mecha":
            page.views.append(
                View(

                    "/mecha",
                    [
                        AppBar(
                            title=Text("Mechatronics",
                                       font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Your Grade", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton("First Grade", color="white", bgcolor=colors.BLUE_500,
                                       width=400, height=100),
                        ElevatedButton(
                            "Second Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                        ElevatedButton(
                            "Third Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                        ElevatedButton(
                            "Fourth Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                    ]
                )
            )
            #################
            ###############
        ###########
        # electro grade
        if page.route == "/electro":
            page.views.append(
                View(

                    "/electro",
                    [
                        AppBar(
                            title=Text("Electronics",
                                       font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Your Grade", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton("First Grade", color="white", bgcolor=colors.BLUE_500,
                                       width=400, height=100),
                        ElevatedButton(
                            "Second Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                        ElevatedButton(
                            "Third Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                        ElevatedButton(
                            "Fourth Grade", color="white", bgcolor=colors.BLUE_500, width=400, height=100),
                    ]
                )
            )
            ################
        ##################
        # sem mecha
        if page.route == "/sem2":
            page.views.append(
                View(
                    "/sem2",
                    [
                        AppBar(
                            title=Text(
                                "Semesters", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Semester", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton(
                            "First Semester", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/mecha")),
                        ElevatedButton(
                            "Second Semester", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/mecha2")),


                    ]
                )
            )
        ##########################
        # sem electro
        if page.route == "/sem3":
            page.views.append(
                View(
                    "/sem3",
                    [
                        AppBar(
                            title=Text(
                                "Semesters", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        Text("Select Semester", width=350,
                             size=40, text_align="center"),
                        Text(""),
                        ElevatedButton(
                            "First Semester", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/electro")),
                        ElevatedButton(
                            "Second Semester", color="white", bgcolor=colors.BLUE_500, width=400, height=100, on_click=lambda _: page.go("/electro2")),


                    ]
                )
            )
        ########
        # comm grad
        if page.route == "/comm2":
            page.views.append(
                View(
                    "/comm2",
                    [
                        AppBar(
                            title=Text(
                                "Specific Graduation Applications", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        # Text("Graduation Applications Will be added Soon"),



                    ]
                )
            )
        ##########
        # electro grad
        if page.route == "/electro2":
            page.views.append(
                View(
                    "/electro2",
                    [
                        AppBar(
                            title=Text(
                                "Specific Graduation Applications", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        # Text("Graduation Applications Will be added Soon"),



                    ]
                )
            )

        ####################
        # mecha grad
        if page.route == "/mecha2":
            page.views.append(
                View(
                    "/mecha2",
                    [
                        AppBar(
                            title=Text(
                                "Specific Graduation Applications", font_family="lemonada"),
                            color="white",
                            bgcolor="black"
                        ),
                        # Text("Graduation Applications Will be added Soon"),



                    ]
                )
            )
        ##############

        page.update()

    def page_go(view):
        page.views.pop()  # function to open new page
        back_page = page.views[-1]  # function to back
        page.go(back_page.route)  # function to تغيير المسار

    page.on_route_change = route_change
    page.on_view_pop = page_go
    page.go(page.route)


app(target=main, assets_dir="assets/")
