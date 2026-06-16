import os
import flet as ft
import flet_video as ftv
import webbrowser
import threading

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Queen Loveness H - Electrical Engineering Portfolio | MineShield App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#fff5f8"
    page.scroll = None

    # =========================================================
    # SOFT BLUSH & PLUSH PINK PROFESSIONAL PALETTE
    # =========================================================
    PRIMARY_PINK = "#b83b5e"           # Deep Blush Pink
    ACCENT_PINK = "#e85d8c"            # Vibrant Soft Pink
    DEEP_ROSE = "#7a2e48"              # Dark rose for text/buttons
    LIGHT_BG = "#fff5f8"               # Soft pink-tint background
    SECTION_PINK = "#fee9f0"
    SECTION_DEEP = "#fdd3e4"
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#5c3b4a"
    AVATAR_BG = "#fee9f0"
    SUBTEXT_GREY = "#a86b8a"
    CARD_BG = "#fffafb"
    BORDER_COLOR = "#f5c2d6"
    
    DARK_CARD_BG = "#7a2e48"
    DARK_TEXT_WHITE = "#ffffff"
    NAV_INACTIVE = "#fdd3e4"
    OVERLAY_PINK = "#e85d8c"
    PROGRESS_TRACK = "#fee9f0"
    SHADOW_PINK = "#e8bfd0"
    CERT_HINT = "#fdd3e4"

    # Global variable to track active dialog
    active_dialog = None

    def open_certificate_zoom(title: str, image_file: str):
        global active_dialog
        
        # Create dialog content
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_PINK, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=f"/images/{image_file}", fit="contain"),
            ),
            actions=[
                ft.TextButton(
                    "Close", 
                    on_click=lambda e: close_certificate_zoom(),
                    style=ft.ButtonStyle(color=PRIMARY_PINK)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        active_dialog = zoom_dialog
        page.show_dialog(zoom_dialog)
        page.update()

    def close_certificate_zoom():
        global active_dialog
        if active_dialog:
            active_dialog.open = False
            active_dialog.update()
            active_dialog = None

    def get_uniform_border(width: int, color: str):
        return ft.Border(
            top=ft.BorderSide(width, color),
            bottom=ft.BorderSide(width, color),
            left=ft.BorderSide(width, color),
            right=ft.BorderSide(width, color),
        )

    # =========================================================
    # PREMIUM COMPONENT BUILDERS
    # =========================================================
    def create_section_header(title: str, subtitle: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    title, 
                    size=28, 
                    weight=ft.FontWeight.BOLD, 
                    color=PRIMARY_PINK, 
                    style=ft.TextStyle(letter_spacing=1.2)
                ),
                ft.Text(subtitle, size=15, color=TEXT_GREY),
                ft.Container(height=4, width=60, bgcolor=ACCENT_PINK, border_radius=2),
                ft.Container(height=15)
            ]
        )

    def create_skill_chip(label: str, level: float):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column([
                ft.Row([
                    ft.Text(label, weight=ft.FontWeight.W_600, color=DEEP_ROSE, size=14),
                    ft.Text(f"{int(level*100)}%", weight=ft.FontWeight.BOLD, color=PRIMARY_PINK, size=12)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=6),
                ft.Stack([
                    ft.Container(height=4, bgcolor=PROGRESS_TRACK, border_radius=2, expand=True),
                    ft.Container(height=4, bgcolor=PRIMARY_PINK, border_radius=2, width=120 * level)
                ])
            ])
        )

    def create_info_card(title: str, body: str, icon=ft.Icons.CHECK_CIRCLE):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=20,
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row([
                        ft.Icon(icon, color=PRIMARY_PINK, size=24),
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                    ]),
                    ft.Text(body, color=TEXT_GREY, size=13),
                ],
            ),
        )

    # =========================================================
    # NAVIGATION SYSTEM
    # =========================================================
    current_page_key = {"value": "overview"}
    nav_buttons = {}

    def build_page_view(section_control, page_key):
        return ft.Column(
            key=f"page-{page_key}",
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=0,
            controls=[section_control],
        )

    def navigate_to(page_key):
        current_page_key["value"] = page_key
        page_switcher.content = build_page_view(portfolio_pages[page_key], page_key)
        for key, button in nav_buttons.items():
            button.style = ft.ButtonStyle(
                color=BG_WHITE if key == page_key else NAV_INACTIVE,
                overlay_color=OVERLAY_PINK,
            )
        page.update()

    # =========================================================
    # SECTIONS DEFINITIONS
    # =========================================================
    
    # 1. Overview Section
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    spacing=15,
                    controls=[
                        ft.Text(
                            "ELECTRICAL ENGINEERING STUDENT @ UNAM", 
                            size=13, 
                            weight=ft.FontWeight.W_600, 
                            color=ACCENT_PINK, 
                            style=ft.TextStyle(letter_spacing=1.5)
                        ),
                        ft.Text("Queen Loveness H", size=42, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                        ft.Text("MineShield App Semester Project Portfolio", size=16, weight=ft.FontWeight.W_500, color=ACCENT_PINK, italic=True),
                        ft.Divider(color=PRIMARY_PINK, thickness=1.5),
                        ft.Text("Phone: +264 81 340 0107  |  Email: tulikeni06@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_ROSE),
                        ft.Text("Electrical Engineering student specializing in power systems, embedded control, signal processing, circuit design, and IoT solutions for mining safety applications. This portfolio is dedicated to my contributions to the MineShield App - a comprehensive mine safety monitoring system.", size=16, color=TEXT_GREY),
                        ft.Container(height=10),
                        ft.ElevatedButton(
                            "Download CV (PDF)",
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor=PRIMARY_PINK,
                            color=BG_WHITE,
                            url="/cv.pdf",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        ),
                    ],
                ),
                ft.Column(
                    col={"sm": 12, "md": 5},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=220,
                            height=220,
                            border_radius=110,
                            bgcolor=AVATAR_BG,
                            alignment=ft.Alignment(0, 0),
                            border=get_uniform_border(4, PRIMARY_PINK),
                            content=ft.Image(src="/images/profile.jpg", width=220, height=220, border_radius=110, fit="cover"),
                        ),
                        ft.Container(height=8),
                        ft.Text("Electrical Engineering & Mine Safety Systems 2026", size=12, color=SUBTEXT_GREY, italic=True),
                    ],
                ),
            ]
        ),
    )

    # 2. Skills Section
    skills_section = ft.Container(
        key="skills",
        bgcolor=SECTION_PINK,
        padding=40,
        content=ft.Column([
            create_section_header("CORE ELECTRICAL & TECHNICAL MATRIX", "Integrated expertise across power systems, control theory, and IoT solutions."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Power & Energy Systems", weight=ft.FontWeight.BOLD, color=ACCENT_PINK, size=16),
                    create_skill_chip("Power System Analysis", 0.88),
                    create_skill_chip("Renewable Energy Integration", 0.85),
                    create_skill_chip("Electrical Machine Design", 0.82),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Control & Embedded Systems", weight=ft.FontWeight.BOLD, color=ACCENT_PINK, size=16),
                    create_skill_chip("MATLAB/Simulink", 0.85),
                    create_skill_chip("Microcontroller Programming", 0.80),
                    create_skill_chip("PLC & SCADA Systems", 0.75),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("IoT & Data Analytics", weight=ft.FontWeight.BOLD, color=ACCENT_PINK, size=16),
                    create_skill_chip("Python for Engineering", 0.82),
                    create_skill_chip("Sensor Networks", 0.78),
                    create_skill_chip("Data Visualization", 0.80),
                ]),
            ], spacing=20)
        ])
    )

    # 3. Individual Portfolio Reflection Section - MineShield App Focus
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD APP - INDIVIDUAL CONTRIBUTION", "Reflection, evidence, lessons learned, challenges, and showcase material."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "MineShield Project Contribution",
                                "I contributed to visitor mode requirements gathering, visitor dashboard testing, read-only verification, and emergency contact validation for the MineShield App.",
                                ft.Icons.SHIELD,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Evidence of Work",
                                "This portfolio includes MATLAB certificate screenshots, visitor demo scripts, APK installation logs, and technical explanations verified during assessment.",
                                ft.Icons.FACT_CHECK,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "I strengthened my ability to test user-facing features, validate emergency protocols, and document visitor-mode requirements for safety-critical applications.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "The main challenge was ensuring read-only verification and visitor dashboard testing. I addressed it by systematic testing, GitHub evidence, and demo scripts.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
                    ],
                ),
                ft.Container(
                    bgcolor=LIGHT_BG,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column([
                                ft.Text("Individual Contribution Video", size=18, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                ft.Text("3-minute visitor demo (View zones/alerts only) plus Q&A for FR-014", color=TEXT_GREY, size=13),
                            ]),
                            ft.TextButton("Video Link Placeholder", icon=ft.Icons.VIDEO_LIBRARY, url="https://example.com/mineshield-demo", style=ft.ButtonStyle(color=ACCENT_PINK)),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 4. Project Timeline Section - Queen Loveness H's Contribution Timeline
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD PROJECT TIMELINE", "Weekly log of my specific contributions to the semester group project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 1-2: Role Assignment & Project Charter", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Assigned as Electrical Systems Lead for MineShield App. Participated in initial meetings, defined visitor mode requirements, and contributed to project charter documentation.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 3-4: Visitor Mode Requirements Gathering", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Gathered and documented visitor mode specifications for the MineShield App, focusing on guest access, view-only permissions, and safety alert visibility.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 5-6: Visitor Dashboard Testing & Read-Only Verification", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Conducted comprehensive testing of the visitor dashboard, verified read-only functionality, and ensured proper access restrictions for guest users.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 7-8: Visitor Demo Script & Emergency Contact Validation", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Created visitor demonstration script for stakeholder presentations and validated emergency contact features for visitor access mode.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 9-10: APK Installation on Phone #3 (Android 11) & Rehearsal", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Successfully installed and tested APK on Android 11 device (Phone #3), performed rehearsal runs for final demonstration.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Final Week: 3-Minute Visitor Demo (View zones/alerts only) & Q&A for FR-014", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("Delivered 3-minute visitor demonstration focusing on view zones and alerts, participated in Q&A session for functional requirement FR-014, and completed final submission.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. Projects Section - MineShield Electrical Focus
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD APP - ELECTRICAL ENGINEERING PROJECTS", "Core electrical systems designed for mine safety monitoring."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("1. MineShield Sensor Network Design", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ft.Text("Multi-sensor array for real-time monitoring of hazardous gas levels, temperature, humidity, and seismic activity in underground mining environments.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("SENSOR NETWORK SPECIFICATIONS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                            ft.Text("• Gas Sensor: MQ-7 (CO detection range 20-2000 ppm)", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• Temperature/Humidity: DHT22 (±0.5°C accuracy)", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• Seismic Sensor: ADXL345 (3-axis accelerometer)", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• Sampling Rate: 100 Hz per sensor channel", size=12, font_family="monospace", color=ACCENT_PINK),
                                        ])
                                    ),
                                    ft.Text("Enables real-time hazard detection with IoT connectivity, data logging, and immediate alert system for mine worker safety.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Arduino/ESP32", size=11, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Sensor Fusion", size=11, color=DEEP_ROSE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("2. Visitor Mode Access Control System", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ft.Text("Secure read-only access system for visitors with view zones and alerts functionality, implementing FR-014 requirements for mine safety monitoring.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("ACCESS CONTROL FEATURES:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                            ft.Text("• Read-only dashboard for visitor accounts", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• View zones: Live hazard monitoring display", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• Alert visibility without modification rights", size=12, font_family="monospace", color=ACCENT_PINK),
                                            ft.Text("• Emergency contact display for visitors", size=12, font_family="monospace", color=ACCENT_PINK),
                                        ])
                                    ),
                                    ft.Text("Ensures safe guest access to mine safety data while maintaining system integrity and data protection protocols.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Android APK", size=11, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Read-Only Mode", size=11, color=DEEP_ROSE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Technical Blog Section - WITH FIXED VIDEO PLAYER
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: ELECTRICAL ENGINEERING CONCEPTS", "Written technical explanations with embedded video demonstration."),
                
                # Blog Post with Video
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=22,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("MineShield App - Electrical Systems Overview", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                            ft.Text("This video demonstrates the MineShield App's electrical monitoring systems, including sensor integration, data visualization, and visitor mode features for mine safety monitoring.", color=TEXT_GREY, size=13),
                            ft.Container(
                                bgcolor=LIGHT_BG,
                                padding=14,
                                border_radius=6,
                                content=ft.Column([
                                    ft.Text("KEY ELECTRICAL COMPONENTS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                    ft.Text("• Multi-sensor array for hazard detection", size=12, color=PRIMARY_PINK),
                                    ft.Text("• Real-time data visualization dashboard", size=12, color=PRIMARY_PINK),
                                    ft.Text("• Visitor mode with read-only access", size=12, color=PRIMARY_PINK),
                                    ft.Text("• Emergency contact validation system", size=12, color=PRIMARY_PINK),
                                ])
                            ),
                            
                            # ── FIXED VIDEO PLAYER ──────────────────────────────────
                            ft.Container(
                                height=400,
                                width=float("inf"),
                                border_radius=8,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                bgcolor=PRIMARY_PINK,
                                content=ftv.Video(
                                    expand=True,
                                    playlist=[
                                        ftv.VideoMedia(
                                            "video/video.mp4"  # Path relative to assets folder
                                        )
                                    ],
                                    playlist_mode=ftv.PlaylistMode.LOOP,
                                    fill_color=PRIMARY_PINK,
                                    aspect_ratio=16/9,
                                    volume=100,
                                    autoplay=True,  # Auto-play when page loads
                                    show_controls=True,
                                    filter_quality=ft.FilterQuality.HIGH,
                                    muted=False,
                                    wakelock=True,
                                ),
                            ),
                            # ── END VIDEO PLAYER ──────────────────────────────
                            
                            ft.Text("Watch this demonstration to see the MineShield App's electrical monitoring capabilities and visitor mode features in action.", color=TEXT_GREY, size=12, italic=True),
                            
                            ft.Divider(color=BORDER_COLOR),
                            
                            ft.Text(
                                "The MineShield App integrates multiple sensor inputs to provide comprehensive mine safety monitoring. My contributions focused on the visitor mode access control system, ensuring guest users can view safety data without modifying critical system settings.",
                                color=TEXT_GREY,
                                size=13,
                            ),
                        ],
                    ),
                ),
                
                # Additional Blog Content
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Ohm's Law & Power Calculations", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ft.Text("For electrical engineering modules, voltage, current, and resistance relationships are fundamental. Correct notation ensures accurate circuit analysis.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("V = I × R   |   P = V × I = I² × R = V²/R", font_family="monospace", size=14, color=PRIMARY_PINK),
                                    ),
                                    ft.Text("Where V is voltage (volts), I is current (amperes), R is resistance (ohms), and P is power (watts).", color=TEXT_GREY, size=13),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Signal Processing for Sensors", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_PINK),
                                    ft.Text("In the MineShield project, structured filtering and signal conditioning helped convert raw sensor data into actionable safety alerts.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("V_out = V_in × (R2/(R1+R2)) | f_c = 1/(2πRC)", font_family="monospace", size=14, color=PRIMARY_PINK),
                                    ),
                                    ft.Text("Voltage dividers and low-pass filters ensure accurate sensor readings by removing high-frequency noise.", color=TEXT_GREY, size=13),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 7. Experience / Leadership Section
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("ELECTRICAL ENGINEERING LEADERSHIP & FIELD EXPERIENCE", "Active contributions to the electrical engineering community and practical industry exposure."),
                ft.Text("Bridging academic electrical theory with practical industry applications while mentoring aspiring electrical engineers.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.WORKSPACE_PREMIUM, color=PRIMARY_PINK, size=28),
                                ft.Text("Mine Safety Systems Intern", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                ft.Text("Assisted in installing and testing environmental monitoring sensors at a local mine. Gained practical experience with data logging from gas and vibration sensors.", color=TEXT_GREY, size=13),
                                ft.Text("• Calibrated CO and methane sensors", size=12, color=TEXT_GREY),
                                ft.Text("• Analyzed sensor data logs for anomalies", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCIENCE, color=PRIMARY_PINK, size=28),
                                ft.Text("Electrical Workshop Facilitator", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                ft.Text("Led a 3-day workshop on Arduino-based data acquisition for 20+ high school students, introducing them to basic circuit design and sensor integration.", color=TEXT_GREY, size=13),
                                ft.Text("• Designed a simple temperature logger", size=12, color=TEXT_GREY),
                                ft.Text("• Supervised student-led mini-projects", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.DOCUMENT_SCANNER, color=PRIMARY_PINK, size=28),
                                ft.Text("Technical Documentation Volunteer", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                ft.Text("Contributed to writing user manuals for a solar-powered water pumping system, helping local technicians with maintenance and troubleshooting.", color=TEXT_GREY, size=13),
                                ft.Text("• Created easy-to-follow wiring diagrams", size=12, color=TEXT_GREY),
                                ft.Text("• Translated technical terms into practical steps", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.CODE, color=PRIMARY_PINK, size=28),
                                ft.Text("MATLAB Student Ambassador", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                ft.Text("Promoted the use of MATLAB and Simulink within my department by organizing study sessions and solving problems collaboratively with peers.", color=TEXT_GREY, size=13),
                                ft.Text("• Assisted 15+ students with lab work", size=12, color=TEXT_GREY),
                                ft.Text("• Shared tips for efficient data plotting", size=12, color=TEXT_GREY),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 8. MATLAB Achievement Hub Section
    certificate_data = [
        {"title": "MATLAB Onramp", "file": "matlab on ramp.jpg"},
        {"title": "Simulink Onramp", "file": "similink matlab.jpg"},
        {"title": "Explore Data with MATLAB Plots", "file": "matlab plots.jpg"},
        {"title": "MATLAB Desktop Tools & Troubleshooting", "file": "troubleshooting.jpg"},
        {"title": "MATLAB Fundamentals", "file": "on ramp matlab.jpg"},
        {"title": "Vectors & Matrices", "file": "vectors and matrices.jpg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        img_control = ft.Image(
            src=f"/images/{cert['file']}",
            height=150,
            fit="contain", 
            scale=1.0,
            animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        )

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG,
            padding=15,
            border_radius=10,
            border=get_uniform_border(1, ACCENT_PINK),
            on_click=lambda e, title=cert["title"], file=cert["file"]: open_certificate_zoom(title, file),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=150,
                        width=320,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        border_radius=6,
                        bgcolor=BG_WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=img_control,
                    ),
                    ft.Container(height=6),
                    ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Click to zoom", color=CERT_HINT, size=11, text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

        hover_stack = ft.Stack(
            height=230,
            controls=[
                ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)
            ]
        )

        def make_hover_handler(stack_wrapper, target_img):
            inner_move_container = stack_wrapper.controls[0]
            def handle_hover(e):
                if e.data == "true":
                    inner_move_container.top = 0  
                    inner_move_container.shadow = ft.BoxShadow(blur_radius=12, color=ACCENT_PINK)
                    target_img.scale = 1.05  
                else:
                    inner_move_container.top = 10  
                    inner_move_container.shadow = None
                    target_img.scale = 1.0
                inner_move_container.update()
                target_img.update()
            return handle_hover

        card_design.on_hover = make_hover_handler(hover_stack, img_control)
        cert_cards.append(ft.Container(col={"sm": 12, "md": 4}, content=hover_stack))

    certification_section = ft.Container(
        key="certificates",
        bgcolor=SECTION_DEEP,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MATLAB ACHIEVEMENT HUB", "Proof of completion for MATLAB and Simulink courses from the MathWorks Learning Center."),
                ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
                ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
            ],
        ),
    )

    # 9. GitHub Evidence & Documentation Section
    github_section = ft.Container(
        key="github",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column([
                            ft.Text("GITHUB EVIDENCE & DOCUMENTATION", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_PINK),
                            ft.Text("Verifiable individual contribution records for the MineShield App semester project team.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=PRIMARY_PINK, tooltip="GitHub Evidence")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Commit History",
                                "Screenshots showing commits authored by Queen Loveness H for visitor mode features, dashboard testing, and read-only verification.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Document proposed features for visitor dashboard, reviews performed, comments resolved, and merges completed for FR-014 implementation.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My code and documentation improved visitor access control, emergency contact validation, and APK deployment testing on Android 11 devices.",
                                ft.Icons.INSIGHTS,
                            ),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.SENSORS, color=PRIMARY_PINK), ft.Text("MineShield-Visitor-Mode", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE)]),
                                    ft.Text("Visitor dashboard with read-only access, view zones for hazard monitoring, and emergency contact display for guest users.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Android", size=10, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Read-Only", size=10, color=DEEP_ROSE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("FR-014", size=10, color=DEEP_ROSE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Android 11 Tested", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_PINK))
                                    ])
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.EMERGENCY, color=PRIMARY_PINK), ft.Text("Emergency-Contact-Validation", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ROSE)]),
                                    ft.Text("Emergency contact verification system for visitor mode with validation protocols and alert testing procedures.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Validation", size=10, color=BG_WHITE), bgcolor=PRIMARY_PINK, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Testing", size=10, color=DEEP_ROSE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Demo Ready", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_PINK))
                                    ])
                                ]
                            )
                        ),
                    ],
                ),
            ],
        ),
    )

    # 10. Advanced Contact Section
    name_field = ft.TextField(
        label="Your Full Name",
        border_color=PRIMARY_PINK,
        focused_border_color=ACCENT_PINK,
        text_style=ft.TextStyle(color=DEEP_ROSE)
    )
    email_field = ft.TextField(
        label="Email Address",
        border_color=PRIMARY_PINK,
        focused_border_color=ACCENT_PINK,
        text_style=ft.TextStyle(color=DEEP_ROSE)
    )
    subject_field = ft.Dropdown(
        label="Subject (Reason for Contact)",
        border_color=PRIMARY_PINK,
        focused_border_color=ACCENT_PINK,
        options=[
            ft.dropdown.Option("Project Collaboration"),
            ft.dropdown.Option("MineShield App Inquiry"),
            ft.dropdown.Option("Research Opportunity"),
            ft.dropdown.Option("Internship/Job Opportunity"),
            ft.dropdown.Option("Technical Question"),
            ft.dropdown.Option("Other"),
        ],
        text_style=ft.TextStyle(color=DEEP_ROSE)
    )
    message_field = ft.TextField(
        label="Detailed Message",
        multiline=True,
        min_lines=5,
        max_lines=8,
        border_color=PRIMARY_PINK,
        focused_border_color=ACCENT_PINK,
        text_style=ft.TextStyle(color=DEEP_ROSE)
    )
    consent_checkbox = ft.Checkbox(
        label="I consent to having Queen Loveness H store my submitted information for the purpose of responding to my inquiry.",
        fill_color=PRIMARY_PINK,
        check_color=BG_WHITE,
        value=False
    )

    def handle_submit_message(e):
        # Validation
        if not name_field.value or not email_field.value or not message_field.value or not subject_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please fill out all required fields (Name, Email, Subject, and Message)."),
                    bgcolor=ACCENT_PINK,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        elif "@" not in email_field.value or "." not in email_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please enter a valid email address."),
                    bgcolor=ACCENT_PINK,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        elif not consent_checkbox.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please consent to the data storage policy before submitting."),
                    bgcolor=ACCENT_PINK,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        else:
            # Simulate sending message
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(f"Thank you {name_field.value}! Your message regarding '{subject_field.value}' has been received. I'll respond to {email_field.value} soon."),
                    bgcolor=PRIMARY_PINK,
                    action="Dismiss",
                    action_color=BG_WHITE,
                    duration=5000
                )
            )
            # Clear form after submission
            name_field.value = ""
            email_field.value = ""
            subject_field.value = None
            message_field.value = ""
            consent_checkbox.value = False
            page.update()

    def clear_form():
        name_field.value = ""
        email_field.value = ""
        subject_field.value = None
        message_field.value = ""
        consent_checkbox.value = False
        page.update()
        page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Form cleared successfully."),
                bgcolor=PRIMARY_PINK,
                action="Close",
                action_color=BG_WHITE
            )
        )

    contact_section = ft.Container(
        key="contact",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Collaborate on electrical engineering projects, MineShield App development, or research opportunities."),
            ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=20,
                        controls=[
                            ft.Text("Available for electrical engineering consultation, IoT sensor network design, power systems analysis, and research collaborations on mine safety technology.", color=TEXT_GREY, size=15),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("📍 Namibia (Electrical Engineering Campus)", color=DEEP_ROSE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("✉️ tulikeni06@gmail.com", color=DEEP_ROSE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("📱 +264 81 340 0107", color=DEEP_ROSE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("⏱ Response time: 24-48 hours", color=TEXT_GREY, size=13),
                            ft.Card(
                                elevation=2,
                                content=ft.Container(
                                    bgcolor=SECTION_PINK,
                                    padding=15,
                                    border_radius=8,
                                    content=ft.Column([
                                        ft.Text("Preferred Contact Methods:", weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                        ft.Text("• Email for project proposals", size=13, color=TEXT_GREY),
                                        ft.Text("• LinkedIn for professional networking", size=13, color=TEXT_GREY),
                                        ft.Text("• Phone for urgent mine safety matters", size=13, color=TEXT_GREY),
                                    ])
                                )
                            )
                        ]
                    ),
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=CARD_BG,
                        padding=30,
                        border_radius=12,
                        border=get_uniform_border(1, BORDER_COLOR),
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                ft.Text("Send a Message About MineShield App or Collaboration", size=18, weight=ft.FontWeight.BOLD, color=DEEP_ROSE),
                                name_field,
                                email_field,
                                subject_field,
                                message_field,
                                consent_checkbox,
                                ft.Divider(color=BORDER_COLOR),
                                ft.Row([
                                    ft.ElevatedButton(
                                        "Submit Message",
                                        icon=ft.Icons.SEND,
                                        bgcolor=PRIMARY_PINK,
                                        color=BG_WHITE,
                                        on_click=handle_submit_message,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6))
                                    ),
                                    ft.TextButton(
                                        "Clear Form",
                                        on_click=lambda e: clear_form(),
                                        style=ft.ButtonStyle(color=ACCENT_PINK)
                                    )
                                ], alignment=ft.MainAxisAlignment.END)
                            ]
                        )
                    )
                ]
            )
        ])
    )

    portfolio_pages = {
        "overview": hero_section,
        "skills": skills_section,
        "contribution": contribution_section,
        "timeline": timeline_section,
        "projects": project_section,
        "blog": blog_section,
        "experience": leadership_section,
        "certificates": certification_section,
        "github": github_section,
        "contact": contact_section,
    }

    page_switcher = ft.AnimatedSwitcher(
        content=build_page_view(hero_section, "overview"),
        duration=220,
        reverse_duration=160,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
        expand=True,
    )

    def make_nav_button(label, page_key):
        button = ft.TextButton(
            label,
            style=ft.ButtonStyle(
                color=BG_WHITE if page_key == current_page_key["value"] else NAV_INACTIVE,
                overlay_color=OVERLAY_PINK,
            ),
            on_click=lambda e, target=page_key: navigate_to(target),
        )
        nav_buttons[page_key] = button
        return button

    # =========================================================
    # STICKY NAVBAR PANEL
    # =========================================================
    header_navbar = ft.Container(
        bgcolor=PRIMARY_PINK,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_PINK)),
        shadow=ft.BoxShadow(blur_radius=10, color=SHADOW_PINK, offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6),
                    ft.Text("QUEEN LOVENESS H", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))
                ], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
                    make_nav_button("Skills", "skills"),
                    make_nav_button("Portfolio", "contribution"),
                    make_nav_button("Timeline", "timeline"),
                    make_nav_button("Projects", "projects"),
                    make_nav_button("Blog", "blog"),
                    make_nav_button("Experience", "experience"),
                    make_nav_button("MATLAB Hub", "certificates"),
                    make_nav_button("GitHub", "github"),
                    make_nav_button("Contact", "contact"),
                ], spacing=10, wrap=True)
            ]
        )
    )

    # =========================================================
    # RENDER DIRECT TO MAIN PAGE WINDOW
    # =========================================================
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                header_navbar,
                page_switcher
            ]
        )
    )

if __name__ == "__main__":
    try:
        # Get port from environment variable or use default
        port = int(os.environ.get("PORT", 8551))
        
        # Run the Flet app in web mode
        ft.app(
            target=main,
            host="0.0.0.0",  # Bind to all interfaces for Render
            port=port,
            assets_dir="assets",
            view=ft.AppView.WEB_BROWSER,
            web_renderer=ft.WebRenderer.CANVAS_KIT,  # Use CanvasKit for better performance
        )
    except Exception as e:
        print(f"Error: {e}", flush=True)
        import traceback
        traceback.print_exc()