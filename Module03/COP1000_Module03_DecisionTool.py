{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMfWOUBMCXck8TpnmS32oAm",
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
        "<a href=\"https://colab.research.google.com/github/AndrewLev34/COP1000-Python/blob/main/Module03/COP1000_Module03_DecisionTool.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5eSqr5hSdzZO",
        "outputId": "987d546d-66f5-48a7-89fb-0e63fe289f20"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is the current Temperature?:107\n",
            "Is it raining?: (yes/no)no\n",
            "Consider going for a swim.\n"
          ]
        }
      ],
      "source": [
        "#Make the yes or no question is case insensitive\n",
        "\n",
        "temp = int(input(\"What is the current Temperature?:\"))\n",
        "rain_status = input(\"Is it raining?: (yes/no)\").lower()\n",
        "\n",
        "if rain_status == \"yes\":\n",
        "  print(\"Consider staying inside today.\")\n",
        "elif rain_status == \"no\" and temp <= 60:\n",
        "  print(\"Consider building a fire outside.\")\n",
        "elif rain_status == \"no\" and 61 <= temp <= 84:\n",
        "  print(\"Consider playing a round of golf.\")\n",
        "elif rain_status == \"no\" and temp >= 85:\n",
        "  print(\"Consider going for a swim.\")\n",
        "else:\n",
        "  print(\"Invalid Response: must answer yes or no\")"
      ]
    }
  ]
}