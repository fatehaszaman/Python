# LeetCode — Graph Algorithms
# Each solution includes Time and Space complexity annotations.

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# GRAPH ALGORITHMS
# =============================================================================

# PROBLEM: Word Ladder (LC 127)
# Time: O(M^2 * N)  — M = word length, N = wordList size; for each word try M positions * 26 letters
# Space: O(M * N)   — queue and visited set store up to N words of length M
def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    word_set = set(wordList)
    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

    return 0

# PROBLEM: Design Twitter (LC 355)
# postTweet:    Time O(1)    | Space O(1)
# follow:       Time O(1)    | Space O(1)
# unfollow:     Time O(1)    | Space O(1)
# getNewsFeed:  Time O(F*T)  | Space O(F*T)  — F followees, T tweets each; sort top 10
# Overall Space: O(U * T + U * F)  — U users, T tweets, F followees per user
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    # Time: O(1) | Space: O(1)
    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    # Time: O(F * T * log(F*T))  — merge and sort all tweets from user + followees
    # Space: O(F * T)
    def getNewsFeed(self, userId):
        all_tweets = []
        all_tweets.extend(self.tweets[userId])
        for followeeId in self.following[userId]:
            all_tweets.extend(self.tweets[followeeId])
        all_tweets.sort(key=lambda x: x[0], reverse=True)
        return [tweet_id for _, tweet_id in all_tweets[:10]]

    # Time: O(1) | Space: O(1)
    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    # Time: O(1) | Space: O(1)
    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)

# PROBLEM: Course Schedule (LC 207)  — Topological Sort / Cycle Detection
# Time: O(V + E)  — V = numCourses, E = len(prerequisites); BFS visits each node and edge once
# Space: O(V + E) — adjacency list and in-degree array
def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    completed = 0
    while queue:
        course = queue.popleft()
        completed += 1
        for dependent in graph[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return completed == numCourses
