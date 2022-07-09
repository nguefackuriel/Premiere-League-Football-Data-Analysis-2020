# #### Plot the the scored and missed goals during the season



plt.figure(figsize=(8,8))

penalties_missed = Total_penalties_attempted - Total_penalties_scored
data = [penalties_missed, Total_penalties_scored ]

cols = ['b', 'r']
#we can add explode parameter to pop out the different sections of our pie chart
#remove explode parameter for a normal pie chart
plt.pie(data, labels = ["missed", "scored"], colors = cols, startangle = 90, shadow = True, explode = (0.1, 0.1), autopct = '%.0f%%')
plt.show()

Nation = df_pl.groupby("Nationality").size().sort_values(ascending = False)
Nation.head(15).plot(kind = 'bar', figsize = (20,8), color = "g")


# So England is the Nationality which have more players followed by France


# #### What is the top 10 clubs which have more players?

Club = df_pl.groupby("Club").size().sort_values(ascending = False)
Club.head(10).plot(kind = 'bar', figsize = (20,8), color = sns.color_palette("magma"))


# #### Let us analyze players based on age group


# For that we will create 4 age group

under_18 = df_pl[df_pl["Age"] <= 18]
between_18_25 = df_pl[(df_pl["Age"] > 18) & (df_pl["Age"] <= 25)]
between_25_32 = df_pl[(df_pl["Age"] > 25) & (df_pl["Age"] <= 32)]
above_32 = df_pl[df_pl["Age"] > 32]



data = np.array([under_18["Name"].count(), between_18_25["Name"].count(),between_25_32["Name"].count(), above_32["Name"].count()])

cols = ['b', 'r', 'g', 'y']
plt.pie(data, labels = ["<18",">18 and <=25", ">25 and <=32", ">32"], colors = cols, startangle = 90, shadow = True, explode = (0.1, 0.1, 0.1, 0.1), autopct = '%.1f%%')
plt.show()


# #### Total under 22 players in each Club



under_22 = df_pl[df_pl["Age"] <= 22]

under_22["Club"].value_counts().head(10).plot(kind = 'bar', figsize = (20,8), color = sns.color_palette("magma"))
plt.show()


# So we have 13 players in the Southampton Club who are <= 22 years old

# Who are them?


under_22[under_22["Club"] == "Southampton"]


# As we can see Moussa Djenepo is the most older of these 13 players in Southampton

# #### Average age of players in each club


plt.figure(figsize = (12,12))
sns.boxplot(x = 'Club', y = 'Age', data = df_pl)
plt.xticks(rotation = 90)


# #### Total assists from each club


assists_per_club = pd.DataFrame(df_pl.groupby("Club", as_index = False)["Assists"].sum())

sns.set_theme(style = "whitegrid", color_codes = True)
plt.figure(figsize=(15,8))
sns.barplot(x = "Club", y = "Assists", data = assists_per_club.sort_values(by = "Assists"), palette = "Set2")
plt.xlabel("Club", fontsize = 30)
plt.ylabel("Assists", fontsize = 20)
plt.xticks(rotation = 90)
plt.title("Clubs vs Assists", fontsize = 20)


# #### Top 15 players assist, their Club, matches, goals


top_15_assists = df_pl[["Name", "Club", "Assists", "Matches", "Goals"]].nlargest(n = 15, columns = "Assists")
top_15_assists


# We can see that Harry Kane has more assist(14), followed by Kevin de Bruyne with 12

# #### What is the number of goals per Clubs? which Club has more goals?


goals_per_club = pd.DataFrame(df_pl.groupby("Club", as_index = False)["Goals"].sum())

sns.set_theme(style = "whitegrid", color_codes = True)
plt.figure(figsize=(15,8))
sns.barplot(x = "Club", y = "Goals", data = goals_per_club.sort_values(by = "Goals"), palette = "Set2")
plt.xlabel("Club", fontsize = 30)
plt.ylabel("Goals", fontsize = 20)
plt.xticks(rotation = 90)
plt.title("Clubs vs Goals", fontsize = 20)


# The information we can get from this graph is that Manchester City was the First of the League 

# #### Top 15 players who assist to the match, their Club, matches, goals


top_15_goals = df_pl[["Name", "Club", "Assists", "Matches", "Goals"]].nlargest(n = 15, columns = "Goals")
top_15_goals


# This table tells us that Harry Kane is the best player with 23 goals, followed by Mohamed Salah from Liverpool with 22 goals. 

# #### Top 15 goals per match


top_15_goals_match = df_pl[["Name", "Club", "Matches", "goal_per_match"]].nlargest(n = 15, columns = "goal_per_match")
top_15_goals_match


# #### Goals with assist and without assist



plt.figure(figsize=(8,8))

assists = df_pl["Assists"].sum()
without_assists = Total_goals - assists
data = [without_assists, assists ]

cols = ['b', 'r']
#we can add explode parameter to pop out the different sections of our pie chart
#remove explode parameter for a normal pie chart
plt.pie(data, labels = ["Goals_without_assists", "Goals_with_assists"], colors = cols, startangle = 90, shadow = True, explode = (0.1, 0.1), autopct = '%.0f%%')
plt.show()


# #### What is the top 5 players with most yellow cards


players_yellow_cards = df_pl.sort_values(by = "Yellow_Cards", ascending = False)[:5]
plt.figure(figsize = (8,6))
plt.title("Players with most Yellow Cards")
sns.barplot(x = players_yellow_cards["Name"], y = players_yellow_cards["Yellow_Cards"], color = "yellow")
plt.xlabel("Name of Players")
plt.ylabel("Number of Yellow Cards")
plt.xticks(rotation = 90)


# So John McGinn is the player with more yellow cards