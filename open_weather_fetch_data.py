{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKobN4XYI9UJKksdMdAmwc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bubblybit23/Complete-Python-3-Bootcamp/blob/master/open_weather_fetch_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LgGSaM63z4KP"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "import pandas as pd\n",
        "\n",
        "# Get data from a public API (e.g., OpenWeather)\n",
        "url = \"https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m\"\n",
        "response = requests.get(url)\n",
        "data = response.json()\n",
        "\n",
        "# Convert to Pandas DataFrame\n",
        "df = pd.DataFrame(data['hourly'])\n",
        "\n",
        "# Save locally\n",
        "df.to_csv(\"weather_data.csv\", index=False)\n",
        "\n",
        "print(\"✅ Data fetched and saved!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N1LQZHSP0JN5",
        "outputId": "40734978-fff2-4d9f-bd3a-896968c05e34"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Data fetched and saved!\n"
          ]
        }
      ]
    }
  ]
}