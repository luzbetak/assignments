#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re

#----------------------------------------------------------------------------------#
def length_of_subsequence_list(nums=[11, 5, 2, 5, 3, 7, 101, 18]):
    """
    Python Questions
    Question 1: Compute the length of the longest strictly
                increasing subsequence in a list.
    Input: nums = [11, 5, 2, 5, 3, 7, 101, 18]

    Output:
    4
    """
    if not nums:
        return 0

    dynamic = [1] * len(nums)
    prev_index = [-1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dynamic[i] < dynamic[j] + 1:
                dynamic[i] = dynamic[j] + 1
                prev_index[i] = j

    result = max(dynamic)

    # Reconstruct the longest increasing subsequence
    lis = []
    index = dynamic.index(result)
    while index != -1:
        lis.append(nums[index])
        index = prev_index[index]

    lis.reverse()
    print("+" + "-" * 70)
    print("| The longest increasing subsequence is:", lis)
    print("| The length is:", result)

#----------------------------------------------------------------------------------#
def list_files_from_url(url="https://gentoo.osuosl.org/distfiles/"):
    """
    Question 2: Write a script to produce a list of every file under
    https://gentoo.osuosl.org/distfiles/.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
    except requests.RequestException as e:
        print(f"Error: Unable to connect to {url}. Details: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all files on the page, excluding directories and links
    files = [
        a['href'] for a in soup.find_all('a', href=True)
        if not a['href'].endswith('/') and not re.match(r"^\?", a['href'])
        and not a['href'].startswith("http")
    ]

    # Print out each file
    for file in files:
        print(f"| {file}")

#----------------------------------------------------------------------------------#
if __name__ == "__main__":
    length_of_subsequence_list()
    print("+" + "-" * 70)
    list_files_from_url()
    print("+" + "-" * 70)

