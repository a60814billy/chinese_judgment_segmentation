#!/usr/local/bin/python3
__author__ = "raccoon"

import random
import math
import sys
from biglaw.read_library import read_library


random.seed()


class Gene:
    score = 0

    def __init__(self, genetic_length):
        self.genetic_length = genetic_length
        self.genetic = list(range(int(self.genetic_length)))

    def get_score(self):
        return self.score


wordsLibrary = read_library('library.txt')

paragraph = sys.argv[1]

GENETIC_LENGTH = len(paragraph) - 1  # 基因長度
POPULATION_CNT = GENETIC_LENGTH * 10  # 母體數量
ITERA_CNT = 200  # 演化次數
CROSSOVER_RATE = 0.7  # 交配率
MUTATION_RATE = 0.05  # 突變率

S = list(range(GENETIC_LENGTH))

population = []  # 母體

print("GENE_LEN:", GENETIC_LENGTH, "POPULATION_COUNT:", POPULATION_CNT, "ITERATION_COUNT:", ITERA_CNT)


def cal_fitness(library, word_set):
    score = 0
    for w in word_set:
        if w in library:
            score += int(math.sqrt(library[w]) * 10) * int(math.pow(len(w), 2))
            # if len(w) == 2 or len(w) == 3:
            # score += int(math.sqrt(library[w])) * math.pow((len(w)), 5)
            # elif len(w) > 4:
            # score += int(math.sqrt(library[w])) * int(math.sqrt(len(w)))
            # else:
            # score += int(math.sqrt(library[w])) * math.pow((len(w)), 2)
        elif len(w) > 10:
            score -= 100
        else:
            score += len(w) * 100
    return score


def user_gene_split_word(sourceword, gene):
    _prev_break_position = 0
    _words = []
    for i in range(len(gene)):
        if gene[i] == 1:
            _words.append(sourceword[_prev_break_position: _prev_break_position + i - _prev_break_position + 1])
            _prev_break_position = i + 1
    if _prev_break_position != len(sourceword):
        _words.append(sourceword[_prev_break_position:len(sourceword)])
    return _words


def reproduction(_mother):
    _pool = []
    total_score = 0
    count = 0

    best_g = None

    for m in _mother:
        if not best_g:
            best_g = m
        elif m.score > best_g.score:
            best_g = m

    _pool.append(best_g)
    _pool.append(best_g)
    _pool.append(best_g)

    count = 3

    for m in _mother:
        total_score += m.score
    for m in _mother:
        cpy_count = int((m.score / total_score) * POPULATION_CNT + 0.5) * 2
        if cpy_count > POPULATION_CNT:
            cpy_count = POPULATION_CNT
        for a in range(cpy_count):
            _pool.append(m)
        count += cpy_count
        if count >= POPULATION_CNT:
            break

    if count < POPULATION_CNT * 2:
        while count < POPULATION_CNT:
            _pool.append(_mother[int(random.random() % len(_mother))])
            count += 1
    return _pool


def crossover(_pool):
    count = 0
    _population = []
    while count < POPULATION_CNT:
        p1 = int(random.random() * POPULATION_CNT)
        p2 = int(random.random() * POPULATION_CNT)
        while p1 == p2:
            p2 = int(random.random() * POPULATION_CNT)

        docrossover = random.random()
        if docrossover > CROSSOVER_RATE:
            _population.append(_pool[p1])
            _population.append(_pool[p2])
            count += 2
        else:
            _p = Gene(GENETIC_LENGTH)
            _rp = int(random.random() * GENETIC_LENGTH)
            for i in range(GENETIC_LENGTH):
                if i < _rp:
                    _p.genetic[i] = _pool[p1].genetic[i]
                else:
                    _p.genetic[i] = _pool[p2].genetic[i]
            _population.append(_p)
            _population.append(_p)
            count += 2
    return _population


def mutation(_population):
    for p in _population:
        if random.random() <= MUTATION_RATE:
            pbit = int(random.random() * GENETIC_LENGTH)
            p.genetic[pbit] = 1 - p.genetic[pbit]
    return _population


def calc_population_score(_population):
    _best_score = 0
    _best_gene = None
    for p in _population:
        words = user_gene_split_word(paragraph, p.genetic)
        p.score = cal_fitness(wordsLibrary, words)
        if p.score > _best_score:
            _best_score = p.score
            _best_gene = p
    return _population, _best_score, _best_gene


for i in range(POPULATION_CNT):
    g = Gene(GENETIC_LENGTH)
    for j in range(GENETIC_LENGTH):
        if int(random.random() * 10) % 2 == 0:
            g.genetic[j] = 1
        else:
            g.genetic[j] = 0
    population.append(g)

# 計算母體的分數

population, best_score, best_gene = calc_population_score(population)

for i in range(ITERA_CNT):
    pool = reproduction(population)
    population = crossover(pool)
    population = mutation(population)
    population.append(best_gene)
    population, best_score, best_gene = calc_population_score(population)

print('Best Result:')
population = sorted(population, key=Gene.get_score, reverse=True)
print(population[0].score, population[0].genetic, user_gene_split_word(paragraph, population[0].genetic))
count = 1

for g in population:
    if g.score < best_score:
        best_score = g.score
        print(g.score, g.genetic, user_gene_split_word(paragraph, g.genetic))
        count += 1
    if count == 3:
        break