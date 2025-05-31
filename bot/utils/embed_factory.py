"""
Emerald's Killfeed - Embed Factory
Advanced embed creation with themed messaging and elite visual design
"""

import discord
from datetime import datetime, timezone
from pathlib import Path
import logging
import random
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

class EmbedFactory:
    """Elite embed factory with 10/10 visual quality and advanced analytics"""

    # Asset paths validation
    ASSETS_PATH = Path('./assets')

    # Enhanced color scheme with gradients and elite styling
    COLORS = {
        'killfeed': 0xFFD700,    # Gold for elite kills
        'suicide': 0xDC143C,     # Crimson red for suicides
        'falling': 0x9370DB,     # Medium slate blue for falling
        'connection': 0x32CD32,  # Lime green for connections
        'mission': 0x4169E1,     # Royal blue for missions
        'airdrop': 0xFF8C00,     # Dark orange for airdrops
        'helicrash': 0xFF4500,   # Orange red for helicrashes
        'trader': 0x9932CC,      # Dark orchid for traders
        'vehicle': 0x696969,     # Dim gray for vehicles
        'success': 0x00FF32,     # Bright green for success
        'error': 0xFF1493,       # Deep pink for errors
        'warning': 0xFFD700,     # Gold for warnings
        'info': 0x00BFFF,        # Deep sky blue for info
        'bounty': 0xFF6347,      # Tomato for bounties
        'economy': 0x7CFC00,     # Lawn green for economy
        'elite': 0xFFD700,       # Gold for elite status
        'legendary': 0xFF00FF     # Magenta for legendary
    }

    # Enhanced themed message pools with military flair - no emojis
    CONNECTION_TITLES = [
        "**OPERATIVE DEPLOYMENT CONFIRMED**",
        "**GHOST PROTOCOL ACTIVATION**", 
        "**COMBAT ASSET MOBILIZED**",
        "**DEATH SQUAD INTEGRATION**",
        "**BLADE RUNNER INSERTION**",
        "**ELITE OPERATIVE ARRIVAL**",
        "**LEGENDARY WARRIOR DETECTED**",
        "**DIAMOND TIER ASSET**",
        "**BATTLEFIELD COMMANDER**",
        "**CHAMPIONS LEAGUE ENTRY**"
    ]

    CONNECTION_DESCRIPTIONS = [
        "**Elite combatant** has entered the war zone",
        "**Legendary operator** joins the apocalypse",
        "**Master tactician** steps into chaos",
        "**Death incarnate** walks among mortals",
        "**Apex predator** enters the hunting grounds",
        "**Mythical warrior** descends from legends",
        "**Unstoppable force** materializes on battlefield",
        "**Living weapon** activates in sector",
        "**God of war** manifests in flesh",
        "**Eternal guardian** awakens for battle"
    ]

    MISSION_READY_TITLES = [
        "**CLASSIFIED OPERATION DECLASSIFIED**",
        "**HIGH-VALUE TARGET ACQUIRED**", 
        "**ELIMINATION CONTRACT ACTIVE**",
        "**DEATH WARRANT AUTHORIZATION**",
        "**BLADE PROTOCOL ENGAGED**",
        "**ELITE MISSION PARAMETERS**",
        "**LEGENDARY OBJECTIVE AVAILABLE**",
        "**DIAMOND TIER OPERATION**",
        "**COMMANDER'S SPECIAL ASSIGNMENT**",
        "**CHAMPIONSHIP ELIMINATION ROUND**"
    ]

    MISSION_READY_DESCRIPTIONS = [
        "**CRITICAL PRIORITY** • Elite operatives required for high-stakes engagement",
        "**MAXIMUM THREAT LEVEL** • Only the deadliest warriors need apply", 
        "**EXPLOSIVE OPPORTUNITY** • Massive rewards await skilled tacticians",
        "**PRECISION STRIKE REQUIRED** • Legendary marksmen to the front lines",
        "**LIGHTNING OPERATION** • Swift execution demanded for success",
        "**INFERNO PROTOCOL** • Enter the flames and emerge victorious",
        "**DEATH'S EMBRACE** • Where angels fear to tread, legends are born",
        "**STELLAR MISSION** • Reach for the stars through fields of fire",
        "**DIAMOND STANDARD** • Only perfection survives this crucible",
        "**CHAMPIONSHIP TIER** • Prove your worth among immortals"
    ]

    # Enhanced killfeed titles with analytics integration - no emojis
    KILL_TITLES = [
        "**COMBAT SUPERIORITY ACHIEVED**",
        "**TARGET NEUTRALIZATION COMPLETE**",
        "**PRECISION ELIMINATION CONFIRMED**",
        "**TACTICAL DOMINANCE DISPLAYED**",
        "**LIGHTNING STRIKE EXECUTED**",
        "**MASTERCLASS ELIMINATION**",
        "**LEGENDARY TAKEDOWN**",
        "**CHAMPIONSHIP KILL**",
        "**BLADE DANCE FINALE**",
        "**ROYAL EXECUTION**"
    ]

    # Gritty survivalist kill messages
    KILL_MESSAGES = [
        "> Another heartbeat silenced beneath the ash sky.",
        "> No burial, no name — just silence where a soul once stood.",
        "> Left no echo. Just scattered gear and cooling blood.",
        "> Cut from the world like thread from a fraying coat.",
        "> Hunger, cold, bullets — it could've been any of them. It was enough.",
        "> Marked, hunted, forgotten. In that order.",
        "> Their fire went out before they even knew they were burning.",
        "> A last breath swallowed by wind and war.",
        "> The price of survival paid in someone else's blood.",
        "> The map didn't change. The player did."
    ]

    SUICIDE_TITLES = [
        "**CRITICAL SYSTEM FAILURE**",
        "**TACTICAL ERROR FATAL**",
        "**OPERATION SELF-DESTRUCT**",
        "**MISSION COMPROMISED**",
        "**EMERGENCY PROTOCOL ACTIVATED**",
        "**SYSTEM OVERLOAD CRITICAL**",
        "**MELTDOWN SEQUENCE COMPLETE**",
        "**OPERATOR DOWN - INTERNAL**",
        "**CHAOS THEORY IN ACTION**",
        "**TRAGIC PERFORMANCE**"
    ]

    # Deadpan dark humor suicide messages
    SUICIDE_MESSAGES = [
        "> Hit \"relocate\" like it was the snooze button. Got deleted.",
        "> Tactical redeployment... into the abyss.",
        "> Rage respawned and logic respawned with it.",
        "> Wanted a reset. Got a reboot straight to the void.",
        "> Pressed something. Paid everything.",
        "> Who needs enemies when you've got bad decisions?",
        "> Alt+F4'd themselves into Valhalla.",
        "> Strategic death — poorly executed.",
        "> Fast travel without a destination.",
        "> Confirmed: the dead menu is not a safe zone."
    ]

    # Enhanced falling death titles - no emojis
    FALLING_TITLES = [
        "**GRAVITY ENFORCEMENT PROTOCOL**",
        "**ALTITUDE ADJUSTMENT FATAL**",
        "**TERMINAL VELOCITY ACHIEVED**",
        "**GROUND IMPACT CONFIRMED**",
        "**ELEVATION ERROR CORRECTED**",
        "**PHYSICS LESSON CONCLUDED**",
        "**DESCENT PROTOCOL FAILED**",
        "**VERTICAL MISCALCULATION**",
        "**FLIGHT PLAN TERMINATED**",
        "**LANDING COORDINATES INCORRECT**"
    ]

    # Sardonic falling messages
    FALLING_MESSAGES = [
        "> Thought they could make it. The ground disagreed.",
        "> Airborne ambition. Terminal results.",
        "> Tried flying. Landed poorly.",
        "> Gravity called. They answered — headfirst.",
        "> Believed in themselves. Gravity didn't.",
        "> From rooftops to regret in under two seconds.",
        "> The sky opened. The floor closed.",
        "> Survival instincts took a coffee break.",
        "> Feet first into a bad decision.",
        "> Their plan had one fatal step too many."
    ]

    # Enhanced airdrop titles - no emojis
    AIRDROP_TITLES = [
        "**TACTICAL SUPPLY DEPLOYMENT**",
        "**HIGH-VALUE CARGO INBOUND**",
        "**GIFT FROM THE GODS**",
        "**TREASURE CHEST DESCENDING**",
        "**LEGENDARY LOOT PACKAGE**",
        "**CHAMPIONSHIP REWARDS**",
        "**LIGHTNING DELIVERY**",
        "**INFERNO SUPPLIES**",
        "**ROYAL CARE PACKAGE**",
        "**PRECISION DROP ZONE**"
    ]

    # Enhanced helicrash titles - no emojis
    HELICRASH_TITLES = [
        "**BIRD OF STEEL GROUNDED**",
        "**AVIATION CATASTROPHE**",
        "**MECHANICAL PHOENIX DOWN**",
        "**SKY CHARIOT TERMINATED**",
        "**IRON ANGEL FALLEN**",
        "**STELLAR CRASH LANDING**",
        "**PRECIOUS METAL SCATTERED**",
        "**CHAMPIONSHIP WRECKAGE**",
        "**TARGET PRACTICE COMPLETE**",
        "**ROYAL AIRCRAFT DOWN**"
    ]

    # Enhanced trader titles - no emojis
    TRADER_TITLES = [
        "**BLACK MARKET MAGNATE**",
        "**SHADOW MERCHANT PRINCE**",
        "**DIAMOND DEALER ACTIVE**",
        "**CHAMPIONSHIP TRADER**",
        "**LIGHTNING MERCHANT**",
        "**INFERNO BUSINESSMAN**",
        "**STELLAR SALESMAN**",
        "**ROYAL ARMS DEALER**",
        "**PRECISION SUPPLIER**",
        "**DEATH'S QUARTERMASTER**"
    ]

    # Mission mappings for readable names
    MISSION_MAPPINGS = {
        'GA_Airport_mis_01_SFPSACMission': 'Airport Mission #1',
        'GA_Airport_mis_02_SFPSACMission': 'Airport Mission #2',
        'GA_Airport_mis_03_SFPSACMission': 'Airport Mission #3',
        'GA_Airport_mis_04_SFPSACMission': 'Airport Mission #4',
        'GA_Military_02_Mis1': 'Military Base Mission #2',
        'GA_Military_03_Mis_01': 'Military Base Mission #3',
        'GA_Military_04_Mis1': 'Military Base Mission #4',
        'GA_Beregovoy_Mis1': 'Beregovoy Settlement Mission',
        'GA_Settle_05_ChernyLog_Mis1': 'Cherny Log Settlement Mission',
        'GA_Ind_01_m1': 'Industrial Zone Mission #1',
        'GA_Ind_02_Mis_1': 'Industrial Zone Mission #2',
        'GA_KhimMash_Mis_01': 'Chemical Plant Mission #1',
        'GA_KhimMash_Mis_02': 'Chemical Plant Mission #2',
        'GA_Bunker_01_Mis1': 'Underground Bunker Mission',
        'GA_Sawmill_01_Mis1': 'Sawmill Mission #1',
        'GA_Settle_09_Mis_1': 'Settlement Mission #9',
        'GA_Military_04_Mis_2': 'Military Base Mission #4B',
        'GA_PromZone_6_Mis_1': 'Industrial Zone Mission #6',
        'GA_PromZone_Mis_01': 'Industrial Zone Mission A',
        'GA_PromZone_Mis_02': 'Industrial Zone Mission B',
        'GA_Kamensk_Ind_3_Mis_1': 'Kamensk Industrial Mission',
        'GA_Kamensk_Mis_1': 'Kamensk City Mission #1',
        'GA_Kamensk_Mis_2': 'Kamensk City Mission #2',
        'GA_Kamensk_Mis_3': 'Kamensk City Mission #3',
        'GA_Krasnoe_Mis_1': 'Krasnoe City Mission',
        'GA_Vostok_Mis_1': 'Vostok City Mission',
        'GA_Lighthouse_02_Mis1': 'Lighthouse Mission #2',
        'GA_Elevator_Mis_1': 'Elevator Complex Mission #1',
        'GA_Elevator_Mis_2': 'Elevator Complex Mission #2',
        'GA_Sawmill_02_1_Mis1': 'Sawmill Mission #2A',
        'GA_Sawmill_03_Mis_01': 'Sawmill Mission #3',
        'GA_Bochki_Mis_1': 'Barrel Storage Mission',
        'GA_Dubovoe_0_Mis_1': 'Dubovoe Resource Mission',
    }

    @staticmethod
    def normalize_mission_name(mission_id: str) -> str:
        """Convert mission ID to readable name"""
        return EmbedFactory.MISSION_MAPPINGS.get(mission_id, mission_id.replace('_', ' ').title())

    @staticmethod
    def get_mission_level(mission_id: str) -> int:
        """Determine mission difficulty level"""
        if any(x in mission_id.lower() for x in ['airport', 'military', 'bunker']):
            return 4  # High difficulty
        elif any(x in mission_id.lower() for x in ['industrial', 'chemical', 'kamensk']):
            return 3  # Medium-high difficulty
        elif any(x in mission_id.lower() for x in ['settlement', 'sawmill']):
            return 2  # Medium difficulty
        else:
            return 1  # Low difficulty

    @staticmethod
    def get_threat_level_display(level: int) -> str:
        """Get enhanced threat level display"""
        threat_displays = {
            1: "**LOW THREAT** - Rookie Operations",
            2: "**MEDIUM THREAT** - Veteran Required", 
            3: "**HIGH THREAT** - Elite Operatives Only",
            4: "**CRITICAL THREAT** - Legendary Masters"
        }
        return threat_displays.get(level, "**UNKNOWN THREAT** - Proceed with Caution")

    @staticmethod
    async def build(embed_type: str, embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build embed with proper file attachment"""
        try:
            if embed_type == 'connection':
                return await EmbedFactory.build_connection_embed(embed_data)
            elif embed_type == 'mission':
                return await EmbedFactory.build_mission_embed(embed_data)
            elif embed_type == 'airdrop':
                return await EmbedFactory.build_airdrop_embed(embed_data)
            elif embed_type == 'helicrash':
                return await EmbedFactory.build_helicrash_embed(embed_data)
            elif embed_type == 'trader':
                return await EmbedFactory.build_trader_embed(embed_data)
            elif embed_type == 'killfeed':
                return await EmbedFactory.build_killfeed_embed(embed_data)
            elif embed_type == 'leaderboard':
                return await EmbedFactory.build_leaderboard_embed(embed_data)
            elif embed_type == 'stats':
                return await EmbedFactory.build_stats_embed(embed_data)
            elif embed_type == 'bounty_set':
                return await EmbedFactory.build_bounty_set_embed(embed_data)
            elif embed_type == 'bounty_list':
                return await EmbedFactory.build_bounty_list_embed(embed_data)
            elif embed_type == 'faction_created':
                return await EmbedFactory.build_faction_created_embed(embed_data)
            elif embed_type == 'economy_balance':
                return await EmbedFactory.build_economy_balance_embed(embed_data)
            elif embed_type == 'economy_work':
                return await EmbedFactory.build_economy_work_embed(embed_data)
            else:
                return await EmbedFactory.build_generic_embed(embed_data)
        except Exception as e:
            logger.error(f"Error building {embed_type} embed: {e}")
            return await EmbedFactory.build_error_embed(f"Failed to build {embed_type} embed")

    @staticmethod
    async def build_connection_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build elite connection embed with enhanced visuals - NO CODE BLOCKS"""
        try:
            title = embed_data.get('title', random.choice(EmbedFactory.CONNECTION_TITLES))
            description = embed_data.get('description', random.choice(EmbedFactory.CONNECTION_DESCRIPTIONS))

            embed = discord.Embed(
                title=title,
                description=description,
                color=EmbedFactory.COLORS['connection'],
                timestamp=datetime.now(timezone.utc)
            )

            player_name = embed_data.get('player_name', 'Unknown Player')
            platform = embed_data.get('platform', 'Unknown')
            server_name = embed_data.get('server_name', 'Unknown Server')

            # Clean professional styling - NO CODE BLOCKS
            embed.add_field(name="**OPERATIVE**", value=f"**{player_name}**", inline=True)
            embed.add_field(name="**PLATFORM**", value=f"*{platform}*", inline=True)
            embed.add_field(name="**DEPLOYMENT ZONE**", value=f"**{server_name}**", inline=True)

            # Enhanced operational status
            embed.add_field(name="**STATUS**", value="**ACTIVE** • *Ready for Combat*", inline=True)
            embed.add_field(name="**CLEARANCE**", value="**AUTHORIZED** • *Full Access*", inline=True)
            embed.add_field(name="**PRIORITY**", value="**HIGH** • *Combat Ready*", inline=True)

            # Enhanced intelligence briefing
            embed.add_field(name="**OPERATIONAL INTELLIGENCE**", 
                          value="Elite combatant has successfully completed deployment protocols and is now fully operational within the designated theater of operations.", 
                          inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            # Create file attachment
            connections_file = discord.File("./assets/Connections.png", filename="Connections.png")
            embed.set_thumbnail(url="attachment://Connections.png")

            return embed, connections_file

        except Exception as e:
            logger.error(f"Error building connection embed: {e}")
            return await EmbedFactory.build_error_embed("Connection embed error")

    @staticmethod
    async def build_mission_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build elite mission embed with enhanced visuals - NO CODE BLOCKS"""
        try:
            mission_id = embed_data.get('mission_id', '')
            state = embed_data.get('state', 'UNKNOWN')
            level = embed_data.get('level', 1)

            # Enhanced state-specific styling
            if state == 'READY':
                title = random.choice(EmbedFactory.MISSION_READY_TITLES)
                description = random.choice(EmbedFactory.MISSION_READY_DESCRIPTIONS)
                color = EmbedFactory.COLORS['mission']
                status_display = "**READY** • *Awaiting Deployment*"
            elif state == 'IN_PROGRESS':
                title = "**OPERATION IN PROGRESS**"
                description = "**ACTIVE ENGAGEMENT** • Elite operatives are currently executing the mission"
                color = 0xFF8C00  # Dark orange for active
                status_display = "**ACTIVE** • *In Progress*"
            elif state == 'COMPLETED':
                title = "**MISSION ACCOMPLISHED**"
                description = "**OPERATION SUCCESS** • All objectives secured with extreme prejudice"
                color = EmbedFactory.COLORS['success']
                status_display = "**COMPLETED** • *Success*"
            else:
                title = "**MISSION STATUS UPDATE**"
                description = "**TACTICAL SITUATION EVOLVING** • Stand by for further orders"
                color = EmbedFactory.COLORS['info']
                status_display = "**UNKNOWN** • *Updating*"

            embed = discord.Embed(
                title=title,
                description=description,
                color=color,
                timestamp=datetime.now(timezone.utc)
            )

            # Enhanced mission details - NO CODE BLOCKS
            mission_name = EmbedFactory.normalize_mission_name(mission_id)
            threat_display = EmbedFactory.get_threat_level_display(level)

            embed.add_field(name="**TARGET DESIGNATION**", 
                          value=f"**{mission_name}**", inline=False)

            embed.add_field(name="**THREAT ASSESSMENT**", 
                          value=threat_display, inline=True)

            embed.add_field(name="**OPERATION STATUS**", 
                          value=status_display, inline=True)

            # Add mission class indicator
            class_indicators = {
                1: "**STANDARD** *Class*",
                2: "**ADVANCED** *Class*", 
                3: "**ELITE** *Class*",
                4: "**LEGENDARY** *Class*"
            }
            embed.add_field(name="**MISSION CLASS**", 
                          value=class_indicators.get(level, "**UNKNOWN** *Class*"), inline=True)

            # Enhanced deployment metrics
            embed.add_field(name="**DIFFICULTY TIER**", value=f"**Level {level}**", inline=True)
            embed.add_field(name="**ENGAGEMENT TYPE**", value="**Direct Combat**", inline=True)
            embed.add_field(name="**EXPECTED DURATION**", value="**Variable**", inline=True)

            # Add call to action
            if state == 'READY':
                embed.add_field(name="**DEPLOYMENT ORDERS**", 
                              value="**Deploy immediately** • High-value rewards await brave operatives. Mission parameters are locked and loaded for immediate execution.", 
                              inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            # Create file attachment
            mission_file = discord.File("./assets/Mission.png", filename="Mission.png")
            embed.set_thumbnail(url="attachment://Mission.png")

            return embed, mission_file

        except Exception as e:
            logger.error(f"Error building mission embed: {e}")
            return await EmbedFactory.build_error_embed("Mission embed error")

    @staticmethod
    async def build_airdrop_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build elite airdrop embed with enhanced visuals - NO CODE BLOCKS"""
        try:
            title = random.choice(EmbedFactory.AIRDROP_TITLES)
            description = "**TACTICAL SUPPLY DROP DETECTED** • High-value military assets incoming"

            embed = discord.Embed(
                title=title,
                description=description,
                color=EmbedFactory.COLORS['airdrop'],
                timestamp=datetime.now(timezone.utc)
            )

            location = embed_data.get('location', 'Classified Location')

            # Professional military briefing format - NO CODE BLOCKS
            embed.add_field(name="**DROP ZONE**", value=f"**{location}**", inline=True)
            embed.add_field(name="**CARGO STATUS**", value="**INBOUND** • *Confirmed*", inline=True)
            embed.add_field(name="**ASSET CLASS**", value="**LEGENDARY TIER**", inline=True)

            # Advanced logistics information
            embed.add_field(name="**DELIVERY METHOD**", value="**Airdrop** • *Parachute Deploy*", inline=True)
            embed.add_field(name="**SECURITY LEVEL**", value="**HIGH VALUE** • *Protected*", inline=True)
            embed.add_field(name="**ACQUISITION WINDOW**", value="**Limited Time** • *Act Fast*", inline=True)

            # Enhanced tactical information
            embed.add_field(name="**TACTICAL INTELLIGENCE**", 
                          value="High competition expected from hostile operatives. Recommend immediate deployment with full combat loadout. Supply drop contains premium military equipment and tactical resources.", 
                          inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            # Create file attachment
            airdrop_file = discord.File("./assets/Airdrop.png", filename="Airdrop.png")
            embed.set_thumbnail(url="attachment://Airdrop.png")

            return embed, airdrop_file

        except Exception as e:
            logger.error(f"Error building airdrop embed: {e}")
            return await EmbedFactory.build_error_embed("Airdrop embed error")

    @staticmethod
    async def build_helicrash_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build elite helicrash embed with enhanced visuals - NO CODE BLOCKS"""
        try:
            title = random.choice(EmbedFactory.HELICRASH_TITLES)
            description = "**AVIATION ASSET COMPROMISED** • Salvage opportunity in hostile territory"

            embed = discord.Embed(
                title=title,
                description=description,
                color=EmbedFactory.COLORS['helicrash'],
                timestamp=datetime.now(timezone.utc)
            )

            location = embed_data.get('location', 'Classified Coordinates')

            # Military crash site analysis - NO CODE BLOCKS
            embed.add_field(name="**CRASH COORDINATES**", value=f"**{location}**", inline=True)
            embed.add_field(name="**RECOVERY STATUS**", value="**SITE LOCATED** • *Active*", inline=True)
            embed.add_field(name="**ASSET CLASS**", value="**MILITARY GRADE**", inline=True)

            # Enhanced crash site intelligence
            embed.add_field(name="**INCIDENT TYPE**", value="**Aviation Failure** • *Mechanical*", inline=True)
            embed.add_field(name="**SALVAGE PRIORITY**", value="**HIGH VALUE** • *Immediate*", inline=True)
            embed.add_field(name="**THREAT ASSESSMENT**", value="**HOSTILE ZONE** • *Dangerous*", inline=True)

            # Comprehensive tactical warning
            embed.add_field(name="**OPERATIONAL WARNING**", 
                          value="Hot zone active with confirmed hostile presence. Approach with maximum caution and full combat readiness. Site contains high-value military equipment but enemy contact is probable.", 
                          inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            # Create file attachment
            helicrash_file = discord.File("./assets/Helicrash.png", filename="Helicrash.png")
            embed.set_thumbnail(url="attachment://Helicrash.png")

            return embed, helicrash_file

        except Exception as e:
            logger.error(f"Error building helicrash embed: {e}")
            return await EmbedFactory.build_error_embed("Helicrash embed error")

    @staticmethod
    async def build_trader_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build elite trader embed with enhanced visuals - NO CODE BLOCKS"""
        try:
            title = random.choice(EmbedFactory.TRADER_TITLES)
            description = "**BLACK MARKET CONTACT ESTABLISHED** • Rare commodities available for trade"

            embed = discord.Embed(
                title=title,
                description=description,
                color=EmbedFactory.COLORS['trader'],
                timestamp=datetime.now(timezone.utc)
            )

            location = embed_data.get('location', 'Secure Location')

            # Professional trading intelligence - NO CODE BLOCKS
            embed.add_field(name="**CONTACT LOCATION**", value=f"**{location}**", inline=True)
            embed.add_field(name="**NETWORK STATUS**", value="**ACTIVE** • *Online*", inline=True)
            embed.add_field(name="**INVENTORY TIER**", value="**ROYAL GRADE**", inline=True)

            # Enhanced trading metrics
            embed.add_field(name="**TRADING STATUS**", value="**Open for Business** • *Available*", inline=True)
            embed.add_field(name="**PAYMENT METHODS**", value="**All Currencies** • *Accepted*", inline=True)
            embed.add_field(name="**STOCK LEVEL**", value="**Premium Items** • *Full Inventory*", inline=True)

            # Professional trade information
            embed.add_field(name="**TRADING INTELLIGENCE**", 
                          value="Premium equipment and rare commodities now available through secure channels. Trader verified and trusted within the network. Bring your best currency for exclusive deals on high-tier military equipment.", 
                          inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            # Create file attachment
            trader_file = discord.File("./assets/Trader.png", filename="Trader.png")
            embed.set_thumbnail(url="attachment://Trader.png")

            return embed, trader_file

        except Exception as e:
            logger.error(f"Error building trader embed: {e}")
            return await EmbedFactory.build_error_embed("Trader embed error")

    @staticmethod
    async def build_killfeed_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build elite killfeed embed with advanced analytics and 10/10 visuals - NO CODE BLOCKS"""
        try:
            is_suicide = embed_data.get('is_suicide', False)
            weapon = embed_data.get('weapon', 'Unknown')
            distance = embed_data.get('distance', 0)

            if is_suicide:
                # Enhanced suicide embed styling - NO CODE BLOCKS
                player_name = embed_data.get('player_name') or embed_data.get('victim', 'Unknown Player')

                if weapon.lower() == 'falling':
                    title = random.choice(EmbedFactory.FALLING_TITLES)
                    color = EmbedFactory.COLORS['falling']
                    themed_description = random.choice(EmbedFactory.FALLING_MESSAGES)
                    asset_file = discord.File("./assets/Falling.png", filename="Falling.png")
                    thumbnail_url = "attachment://Falling.png"
                    status_display = "**KIA - FALLING** • *Non-Combat Loss*"
                else:
                    title = random.choice(EmbedFactory.SUICIDE_TITLES)
                    color = EmbedFactory.COLORS['suicide']
                    themed_description = random.choice(EmbedFactory.SUICIDE_MESSAGES)
                    asset_file = discord.File("./assets/Suicide.png", filename="Suicide.png")
                    thumbnail_url = "attachment://Suicide.png"
                    status_display = "**KIA - INTERNAL** • *System Failure*"

                embed = discord.Embed(
                    title=title,
                    color=color,
                    timestamp=datetime.now(timezone.utc)
                )

                # Professional incident report - NO CODE BLOCKS
                embed.add_field(name="**OPERATIVE**", value=f"**{player_name}**", inline=True)
                embed.add_field(name="**CAUSE OF DEATH**", value=f"*{weapon}*", inline=True)
                embed.add_field(name="**STATUS**", value=status_display, inline=True)

                # Enhanced incident analysis
                embed.add_field(name="**INCIDENT TYPE**", value="**Non-Combat Loss** • *Internal*", inline=True)
                embed.add_field(name="**THREAT LEVEL**", value="**Self-Inflicted** • *No Enemy*", inline=True)
                embed.add_field(name="**RESPONSE STATUS**", value="**Documented** • *Recorded*", inline=True)

                # Enhanced mission report
                embed.add_field(name="**INCIDENT REPORT**", value=themed_description, inline=False)

                embed.set_thumbnail(url=thumbnail_url)

            else:
                # Enhanced PvP kill embed with advanced analytics - NO CODE BLOCKS
                killer = embed_data.get('killer', 'Unknown')
                victim = embed_data.get('victim', 'Unknown')
                killer_kdr = embed_data.get('killer_kdr', '0.00')
                victim_kdr = embed_data.get('victim_kdr', '0.00')
                title = random.choice(EmbedFactory.KILL_TITLES)

                # Advanced analytics calculations
                try:
                    killer_kdr_float = float(killer_kdr)
                    victim_kdr_float = float(victim_kdr)

                    # Performance tier calculation
                    def get_performance_tier(kdr):
                        if kdr >= 3.0:
                            return "**LEGENDARY** *Tier*"
                        elif kdr >= 2.0:
                            return "**ELITE** *Tier*"
                        elif kdr >= 1.5:
                            return "**VETERAN** *Tier*"
                        elif kdr >= 1.0:
                            return "**SKILLED** *Tier*"
                        else:
                            return "**ROOKIE** *Tier*"

                    killer_tier = get_performance_tier(killer_kdr_float)
                    victim_tier = get_performance_tier(victim_kdr_float)

                    # Engagement analysis
                    if distance > 500:
                        range_class = "**LONG RANGE** • *Sniper Elite*"
                        range_type = "**Precision Engagement**"
                    elif distance > 200:
                        range_class = "**MEDIUM RANGE** • *Tactical Combat*"
                        range_type = "**Standard Engagement**"
                    elif distance > 50:
                        range_class = "**CLOSE RANGE** • *Intense Combat*"
                        range_type = "**Close Quarters**"
                    else:
                        range_class = "**POINT BLANK** • *Execution Style*"
                        range_type = "**Direct Contact**"

                except:
                    killer_tier = "**ROOKIE** *Tier*"
                    victim_tier = "**ROOKIE** *Tier*"
                    range_class = "**STANDARD** • *Engagement*"
                    range_type = "**Combat Encounter**"

                embed = discord.Embed(
                    title=title,
                    color=EmbedFactory.COLORS['killfeed'],
                    timestamp=datetime.now(timezone.utc)
                )

                # Enhanced combat participants - NO CODE BLOCKS
                embed.add_field(name="**VICTOR**", 
                              value=f"**{killer}**\n{killer_tier} • **{killer_kdr}** *KDR*", 
                              inline=True)

                embed.add_field(name="**ELIMINATED**", 
                              value=f"**{victim}**\n{victim_tier} • **{victim_kdr}** *KDR*", 
                              inline=True)

                embed.add_field(name="**WEAPON SYSTEM**", 
                              value=f"**{weapon}**", 
                              inline=True)

                # Advanced engagement analytics
                if distance > 0:
                    embed.add_field(name="**ENGAGEMENT RANGE**", 
                                  value=f"**{distance:.1f}m**\n{range_class}", 
                                  inline=True)

                    embed.add_field(name="**ENGAGEMENT TYPE**", 
                                  value=range_type, 
                                  inline=True)

                # Skill gap analysis
                try:
                    skill_gap = abs(killer_kdr_float - victim_kdr_float)
                    if skill_gap > 1.0:
                        skill_analysis = "**SKILL GAP** • *Significant Difference*"
                    elif skill_gap > 0.5:
                        skill_analysis = "**MATCHED** • *Even Skills*"
                    else:
                        skill_analysis = "**CLOSE FIGHT** • *Nearly Equal*"

                    embed.add_field(name="**COMBAT ANALYSIS**", 
                                  value=skill_analysis, inline=True)
                except:
                    embed.add_field(name="**COMBAT ANALYSIS**", 
                                  value="**ENGAGEMENT** • *Standard*", inline=True)

                # Enhanced combat report with random message
                kill_message = random.choice(EmbedFactory.KILL_MESSAGES)
                embed.add_field(name="**COMBAT REPORT**", value=kill_message, inline=False)

                asset_file = discord.File("./assets/Killfeed.png", filename="Killfeed.png")
                embed.set_thumbnail(url="attachment://Killfeed.png")

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            return embed, asset_file

        except Exception as e:
            logger.error(f"Error building killfeed embed: {e}")
            return await EmbedFactory.build_error_embed("Killfeed embed error")

    @staticmethod
    async def build_leaderboard_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced leaderboard embed with 10/10 visuals - NO CODE BLOCKS"""
        try:
            title = embed_data.get('title', "**ELITE COMBAT RANKINGS**")
            description = embed_data.get('description', '**Champions ranked by battlefield supremacy**')

            embed = discord.Embed(
                title=title,
                description=description,
                color=EmbedFactory.COLORS['elite'],
                timestamp=datetime.now(timezone.utc)
            )

            # Enhanced rankings display - NO CODE BLOCKS
            rankings = embed_data.get('rankings', '')
            if rankings:
                embed.add_field(name="**HALL OF LEGENDS**", value=rankings, inline=False)

            # Enhanced statistics - NO CODE BLOCKS
            total_kills = embed_data.get('total_kills', 0)
            total_deaths = embed_data.get('total_deaths', 0)
            stat_type = embed_data.get('stat_type', 'general')

            if total_kills > 0 or total_deaths > 0:
                if stat_type == 'kills':
                    embed.add_field(name="**TOTAL ELIMINATIONS**", value=f"**{total_kills:,}**", inline=True)
                elif stat_type == 'deaths':
                    embed.add_field(name="**TOTAL CASUALTIES**", value=f"**{total_deaths:,}**", inline=True)
                elif stat_type == 'kdr':
                    total_kdr = total_kills / max(total_deaths, 1) if total_deaths > 0 else total_kills
                    embed.add_field(name="**AVERAGE EFFICIENCY**", value=f"**{total_kdr:.2f}**", inline=True)

            # Server context - NO CODE BLOCKS
            server_name = embed_data.get('server_name', 'All Servers')
            embed.add_field(name="**THEATER OF OPERATIONS**", value=f"**{server_name}**", inline=True)

            # Enhanced competitive metrics
            embed.add_field(name="**RANKING SYSTEM**", value="**Live Rankings** • *Real-time*", inline=True)
            embed.add_field(name="**UPDATE FREQUENCY**", value="**Dynamic** • *Continuous*", inline=True)
            embed.add_field(name="**COMPETITION LEVEL**", value="**Elite Tier** • *Champions Only*", inline=True)

            # Determine thumbnail
            thumbnail_url = embed_data.get('thumbnail_url', 'attachment://Leaderboard.png')
            if 'WeaponStats.png' in thumbnail_url:
                asset_file = discord.File("./assets/WeaponStats.png", filename="WeaponStats.png")
            elif 'Faction.png' in thumbnail_url:
                asset_file = discord.File("./assets/Faction.png", filename="Faction.png")
            else:
                asset_file = discord.File("./assets/Leaderboard.png", filename="Leaderboard.png")

            embed.set_thumbnail(url=thumbnail_url)
            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            return embed, asset_file

        except Exception as e:
            logger.error(f"Error building leaderboard embed: {e}")
            return await EmbedFactory.build_error_embed("Leaderboard embed error")

    @staticmethod
    async def build_stats_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced stats embed with 10/10 visuals - NO CODE BLOCKS"""
        try:
            player_name = embed_data.get('player_name', 'Unknown Player')
            server_name = embed_data.get('server_name', 'Unknown Server')

            title = "**ELITE OPERATOR PROFILE**"
            description = f"**Comprehensive battlefield analysis for** ***{player_name}***"

            embed = discord.Embed(
                title=title,
                description=description,
                color=EmbedFactory.COLORS['info'],
                timestamp=datetime.now(timezone.utc)
            )

            # Enhanced statistics with validation - NO CODE BLOCKS
            kills = max(0, embed_data.get('kills', 0))
            deaths = max(0, embed_data.get('deaths', 0))
            kdr_value = embed_data.get('kdr', '0.00')

            # KDR formatting
            try:
                if isinstance(kdr_value, (int, float)):
                    kdr = f"{float(kdr_value):.2f}"
                else:
                    kdr = str(kdr_value)
            except:
                kdr = "0.00"

            # Core combat metrics - NO CODE BLOCKS
            embed.add_field(name="**ELIMINATIONS**", value=f"**{kills:,}**", inline=True)
            embed.add_field(name="**CASUALTIES**", value=f"**{deaths:,}**", inline=True)
            embed.add_field(name="**EFFICIENCY RATIO**", value=f"**{kdr}**", inline=True)

            # Additional enhanced metrics - NO CODE BLOCKS
            personal_best_distance = float(embed_data.get('personal_best_distance', 0.0))
            favorite_weapon = embed_data.get('favorite_weapon')
            best_streak = max(0, embed_data.get('best_streak', 0))
            suicides = max(0, embed_data.get('suicides', 0))

            if personal_best_distance > 0:
                if personal_best_distance >= 1000:
                    distance_str = f"{personal_best_distance/1000:.1f}km"
                else:
                    distance_str = f"{personal_best_distance:.0f}m"
                embed.add_field(name="**LONGEST SHOT**", value=f"**{distance_str}**", inline=True)

            if favorite_weapon and favorite_weapon != 'None' and favorite_weapon.strip():
                embed.add_field(name="**PREFERRED WEAPON**", value=f"**{favorite_weapon}**", inline=True)

            if best_streak > 0:
                embed.add_field(name="**BEST STREAK**", value=f"**{best_streak:,}**", inline=True)

            if suicides > 0:
                embed.add_field(name="**NON-COMBAT LOSSES**", value=f"**{suicides:,}**", inline=True)

            # Enhanced operational context - NO CODE BLOCKS
            embed.add_field(name="**THEATER OF OPERATIONS**", value=f"**{server_name}**", inline=False)

            # Enhanced tactical assessment - NO CODE BLOCKS
            if kills > 0 or deaths > 0:
                total_engagements = kills + deaths
                survival_rate = (kills / total_engagements * 100) if total_engagements > 0 else 0

                if survival_rate >= 70:
                    performance_rank = "**LEGENDARY OPERATIVE** • *Apex Tier*"
                elif survival_rate >= 50:
                    performance_rank = "**ELITE SOLDIER** • *Master Tier*"
                elif survival_rate >= 30:
                    performance_rank = "**VETERAN FIGHTER** • *Expert Tier*"
                else:
                    performance_rank = "**ACTIVE COMBATANT** • *Standard Tier*"

                embed.add_field(name="**TACTICAL ASSESSMENT**", 
                               value=f"{performance_rank}\n"
                                     f"**{total_engagements:,}** *total engagements*\n"
                                     f"**{survival_rate:.1f}%** *success rate*", 
                               inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            main_file = discord.File("./assets/WeaponStats.png", filename="WeaponStats.png")
            embed.set_thumbnail(url="attachment://WeaponStats.png")

            return embed, main_file

        except Exception as e:
            logger.error(f"Error building stats embed: {e}")
            return await EmbedFactory.build_error_embed("Stats embed error")

    @staticmethod
    async def build_generic_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced generic embed - NO CODE BLOCKS"""
        try:
            embed = discord.Embed(
                title=embed_data.get('title', '**EMERALD SERVERS**'),
                description=embed_data.get('description', '**Elite Gaming Network Notification**'),
                color=EmbedFactory.COLORS['info'],
                timestamp=datetime.now(timezone.utc)
            )

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            main_file = discord.File("./assets/main.png", filename="main.png")
            embed.set_thumbnail(url="attachment://main.png")

            return embed, main_file

        except Exception as e:
            logger.error(f"Error building generic embed: {e}")
            return await EmbedFactory.build_error_embed("Generic embed error")

    @staticmethod
    async def build_bounty_set_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced bounty set embed - NO CODE BLOCKS"""
        try:
            title = "**ELIMINATION CONTRACT ISSUED**"

            embed = discord.Embed(
                title=title,
                description=f"**High-value target designated:** ***{embed_data['target_character']}***",
                color=EmbedFactory.COLORS['bounty'],
                timestamp=datetime.now(timezone.utc)
            )

            # Professional contract details - NO CODE BLOCKS
            embed.add_field(name="**REWARD**", value=f"**${embed_data['bounty_amount']:,}**", inline=True)
            embed.add_field(name="**TARGET**", value=f"**{embed_data['target_character']}**", inline=True)
            embed.add_field(name="**EXPIRES**", value=f"<t:{embed_data['expires_timestamp']}:R>", inline=True)

            # Enhanced contract details
            embed.add_field(name="**CONTRACT TYPE**", value="**Elimination** • *Lethal Force*", inline=True)
            embed.add_field(name="**PAYMENT STATUS**", value="**Guaranteed** • *Upon Completion*", inline=True)
            embed.add_field(name="**PRIORITY LEVEL**", value="**High Value** • *Priority Target*", inline=True)

            embed.add_field(name="**EXECUTION INSTRUCTIONS**", 
                          value="**Eliminate target to claim bounty.** Contract completion requires confirmed elimination of designated target. Payment will be processed immediately upon verification of target neutralization.", 
                          inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            bounty_file = discord.File("./assets/Bounty.png", filename="Bounty.png")
            embed.set_thumbnail(url="attachment://Bounty.png")

            return embed, bounty_file

        except Exception as e:
            logger.error(f"Error building bounty set embed: {e}")
            return await EmbedFactory.build_error_embed("Bounty set embed error")

    @staticmethod
    async def build_bounty_list_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced bounty list embed - NO CODE BLOCKS"""
        try:
            embed = discord.Embed(
                title="**ACTIVE ELIMINATION CONTRACTS**",
                description=f"**{embed_data['total_bounties']}** *high-value targets identified*",
                color=EmbedFactory.COLORS['bounty'],
                timestamp=datetime.now(timezone.utc)
            )

            bounty_list = []
            for i, bounty in enumerate(embed_data['bounty_list'], 1):
                target = bounty['target_character']
                amount = bounty['amount']
                expires = bounty['expires_at']
                auto_indicator = " *Auto*" if bounty.get('auto_generated', False) else ""

                bounty_list.append(
                    f"**{i}.** **{target}** - **${amount:,}**{auto_indicator}\n"
                    f"    *Expires* <t:{int(expires.timestamp())}:R>"
                )

            embed.add_field(name="**CONTRACT LIST**", value="\n".join(bounty_list), inline=False)

            if embed_data.get('showing_partial'):
                embed.add_field(name="**STATUS**", value="*Showing top 10 contracts*", inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            bounty_file = discord.File("./assets/Bounty.png", filename="Bounty.png")
            embed.set_thumbnail(url="attachment://Bounty.png")

            return embed, bounty_file

        except Exception as e:
            logger.error(f"Error building bounty list embed: {e}")
            return await EmbedFactory.build_error_embed("Bounty list embed error")

    @staticmethod
    async def build_faction_created_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced faction created embed - NO CODE BLOCKS"""
        try:
            embed = discord.Embed(
                title="**FACTION ESTABLISHED**",
                description=f"**New military organization formed:** ***{embed_data['faction_name']}***",
                color=EmbedFactory.COLORS['success'],
                timestamp=datetime.now(timezone.utc)
            )

            # Professional organizational details - NO CODE BLOCKS
            embed.add_field(name="**COMMANDER**", value=f"**{embed_data['leader']}**", inline=True)

            if embed_data.get('faction_tag'):
                embed.add_field(name="**DESIGNATION**", value=f"**[{embed_data['faction_tag']}]**", inline=True)

            embed.add_field(name="**ROSTER**", 
                          value=f"**{embed_data['member_count']}**/*{embed_data['max_members']}*", 
                          inline=True)

            # Enhanced organizational metrics
            embed.add_field(name="**STATUS**", value="**Active** • *Operational*", inline=True)
            embed.add_field(name="**RECRUITMENT**", value="**Open** • *Accepting Members*", inline=True)
            embed.add_field(name="**COMMAND STRUCTURE**", value="**Hierarchical** • *Military*", inline=True)

            embed.add_field(name="**OPERATIONAL DIRECTIVES**", 
                          value="**Use `/faction invite` to recruit members** • Expand your organization with skilled operatives.\n"
                                "**Use `/faction settings` to configure options** • Customize faction parameters and policies.", 
                          inline=False)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            faction_file = discord.File("./assets/Faction.png", filename="Faction.png")
            embed.set_thumbnail(url="attachment://Faction.png")

            return embed, faction_file

        except Exception as e:
            logger.error(f"Error building faction created embed: {e}")
            return await EmbedFactory.build_error_embed("Faction creation embed error")

    @staticmethod
    async def build_economy_balance_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced economy balance embed - NO CODE BLOCKS"""
        try:
            embed = discord.Embed(
                title="**FINANCIAL STATUS REPORT**",
                description=f"***{embed_data['user_name']}'s*** **economic portfolio**",
                color=EmbedFactory.COLORS['economy'],
                timestamp=datetime.now(timezone.utc)
            )

            # Professional financial metrics - NO CODE BLOCKS
            embed.add_field(name="**CURRENT BALANCE**", value=f"**${embed_data['balance']:,}**", inline=True)
            embed.add_field(name="**TOTAL EARNED**", value=f"**${embed_data['total_earned']:,}**", inline=True)
            embed.add_field(name="**TOTAL SPENT**", value=f"**${embed_data['total_spent']:,}**", inline=True)

            # Enhanced financial analysis
            net_worth = embed_data['total_earned'] - embed_data['total_spent']
            embed.add_field(name="**NET WORTH**", value=f"**${net_worth:,}**", inline=True)
            embed.add_field(name="**ACCOUNT STATUS**", value="**Active** • *Good Standing*", inline=True)
            embed.add_field(name="**CREDIT RATING**", value="**Excellent** • *Verified*", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            main_file = discord.File("./assets/main.png", filename="main.png")
            embed.set_thumbnail(url="attachment://main.png")

            return embed, main_file

        except Exception as e:
            logger.error(f"Error building economy balance embed: {e}")
            return await EmbedFactory.build_error_embed("Economy balance embed error")

    @staticmethod
    async def build_economy_work_embed(embed_data: dict) -> tuple[discord.Embed, discord.File]:
        """Build enhanced economy work embed - NO CODE BLOCKS"""
        try:
            embed = discord.Embed(
                title="**MISSION COMPLETED**",
                description=f"**{embed_data['scenario']}**",
                color=EmbedFactory.COLORS['success'],
                timestamp=datetime.now(timezone.utc)
            )

            # Professional compensation details - NO CODE BLOCKS
            embed.add_field(name="**COMPENSATION**", value=f"**+${embed_data['earnings']:,}**", inline=True)
            embed.add_field(name="**NEXT ASSIGNMENT**", value="**Available in 1 hour**", inline=True)
            embed.add_field(name="**MISSION STATUS**", value="**Completed** • *Success*", inline=True)

            # Enhanced work metrics
            embed.add_field(name="**PERFORMANCE RATING**", value="**Excellent** • *Above Standard*", inline=True)
            embed.add_field(name="**ASSIGNMENT TYPE**", value="**Contract Work** • *Freelance*", inline=True)
            embed.add_field(name="**PAYMENT STATUS**", value="**Processed** • *Immediate*", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            main_file = discord.File("./assets/main.png", filename="main.png")
            embed.set_thumbnail(url="attachment://main.png")

            return embed, main_file

        except Exception as e:
            logger.error(f"Error building economy work embed: {e}")
            return await EmbedFactory.build_error_embed("Economy work embed error")

    @staticmethod
    async def build_error_embed(error_message: str) -> tuple[discord.Embed, discord.File]:
        """Build enhanced error embed - NO CODE BLOCKS"""
        try:
            embed = discord.Embed(
                title="**SYSTEM ERROR**",
                description=f"**Critical malfunction detected:** *{error_message}*",
                color=EmbedFactory.COLORS['error'],
                timestamp=datetime.now(timezone.utc)
            )

            # Professional error reporting - NO CODE BLOCKS
            embed.add_field(name="**STATUS**", value="**OPERATION FAILED** • *Error*", inline=True)
            embed.add_field(name="**ACTION REQUIRED**", value="**DIAGNOSTIC NEEDED** • *Investigation*", inline=True)
            embed.add_field(name="**PRIORITY**", value="**High** • *Immediate Attention*", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")

            main_file = discord.File("./assets/main.png", filename="main.png")
            embed.set_thumbnail(url="attachment://main.png")

            return embed, main_file

        except Exception as e:
            logger.error(f"Critical error building error embed: {e}")
            embed = discord.Embed(
                title="**CRITICAL ERROR**",
                description="**Multiple system failures detected**",
                color=0xFF0000,
                timestamp=datetime.now(timezone.utc)
            )
            fallback_file = discord.File("./assets/main.png", filename="main.png")
            return embed, fallback_file

    # Legacy compatibility methods (unchanged)
    @staticmethod
    def create_mission_embed(title: str, description: str, mission_id: str, level: int, state: str, respawn_time: int = None) -> discord.Embed:
        """Create mission embed (legacy compatibility)"""
        try:
            if state == 'READY':
                color = EmbedFactory.COLORS['mission']
            elif state == 'IN_PROGRESS':
                color = 0xFFAA00
            elif state == 'COMPLETED':
                color = EmbedFactory.COLORS['success']
            else:
                color = EmbedFactory.COLORS['info']

            embed = discord.Embed(
                title=title,
                description=description,
                color=color,
                timestamp=datetime.now(timezone.utc)
            )

            mission_name = EmbedFactory.normalize_mission_name(mission_id)
            embed.add_field(name="📍 Mission", value=mission_name, inline=False)

            threat_levels = ["Low", "Medium", "High", "Critical"]
            threat_level = threat_levels[min(level-1, 3)] if level > 0 else "Unknown"
            embed.add_field(name="Threat Level", value=f"Class {level} - {threat_level}", inline=True)
            embed.add_field(name="Status", value=state.replace('_', ' ').title(), inline=True)

            if respawn_time:
                embed.add_field(name="Respawn", value=f"{respawn_time}s", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")
            embed.set_thumbnail(url="attachment://Mission.png")

            return embed

        except Exception as e:
            logger.error(f"Error creating mission embed: {e}")
            return discord.Embed(title="Error", description="Failed to create mission embed", color=0xFF0000)

    @staticmethod
    def create_airdrop_embed(state: str, location: str, timestamp: datetime) -> discord.Embed:
        """Create airdrop embed (legacy compatibility)"""
        try:
            embed = discord.Embed(
                title="🪂 Airdrop Incoming",
                description="High-value supply drop detected inbound",
                color=EmbedFactory.COLORS['airdrop'],
                timestamp=timestamp
            )

            embed.add_field(name="📍 Drop Zone", value=location, inline=True)
            embed.add_field(name="⏰ Status", value=state.title(), inline=True)
            embed.add_field(name="💰 Contents", value="High-Value Loot", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")
            embed.set_thumbnail(url="attachment://Airdrop.png")

            return embed

        except Exception as e:
            logger.error(f"Error creating airdrop embed: {e}")
            return discord.Embed(title="Error", description="Failed to create airdrop embed", color=0xFF0000)

    @staticmethod
    def create_helicrash_embed(location: str, timestamp: datetime) -> discord.Embed:
        """Create helicrash embed (legacy compatibility)"""
        try:
            embed = discord.Embed(
                title="🚁 Helicopter Crash",
                description="Military helicopter has crashed - salvage opportunity detected",
                color=EmbedFactory.COLORS['helicrash'],
                timestamp=timestamp
            )

            embed.add_field(name="💥 Crash Site", value=location, inline=True)
            embed.add_field(name="⚠️ Status", value="Active", inline=True)
            embed.add_field(name="🎖️ Loot Type", value="Military Equipment", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")
            embed.set_thumbnail(url="attachment://Helicrash.png")

            return embed

        except Exception as e:
            logger.error(f"Error creating helicrash embed: {e}")
            return discord.Embed(title="Error", description="Failed to create helicrash embed", color=0xFF0000)

    @staticmethod
    def create_trader_embed(location: str, timestamp: datetime) -> discord.Embed:
        """Create trader embed (legacy compatibility)"""
        try:
            embed = discord.Embed(
                title="🏪 Trader Arrival",
                description="Traveling merchant has arrived with rare goods",
                color=EmbedFactory.COLORS['trader'],
                timestamp=timestamp
            )

            embed.add_field(name="📍 Location", value=location, inline=True)
            embed.add_field(name="⏰ Status", value="Open for Business", inline=True)
            embed.add_field(name="💎 Inventory", value="Rare Items Available", inline=True)

            embed.set_footer(text="Powered by Emerald", url="https://discord.gg/EmeraldServers")
            embed.set_thumbnail(url="attachment://Trader.png")

            return embed

        except Exception as e:
            logger.error(f"Error creating trader embed: {e}")
            return discord.Embed(title="Error", description="Failed to create trader embed", color=0xFF0000)