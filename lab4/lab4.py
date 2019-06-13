# https://github.com/Yelp/mrjob/blob/master/docs/guides/quickstart.rst
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from mrjob.protocol import TextProtocol

WORD_RE = re.compile(r"[\w']+")


class MRMostUsedWord(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper_get_words(self, _, line):
        # yield each word in the line
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        # optimization: sum the words we've seen so far
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        yield None, (sum(counts), word)

    # discard the key; it is just None
    def reducer_find_max_word(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        last_max = 999999999999999999999999999999999999999
        wordlist = list()
        tempword = list()
        for each in word_count_pairs:
            wordlist.append(each)
        temp = (1, '')
        for _ in range(0, 15):
            m = 0
            tempword.append(temp[1])
            for pair in wordlist:
                if pair[0] > m and pair[0] <= last_max and not pair[1] in tempword:
                    m = pair[0]
                    temp = pair
            last_max = m
            yield str(temp[0]), temp[1]

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)

        ]


if __name__ == '__main__':
    MRMostUsedWord.run()
