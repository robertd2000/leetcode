function commonChars2(words: string[]): string[] {
  let last = count(words[0]);
  for (let i = 1; i < words.length; i++) {
    last = intersection(last, count(words[i]));
  }

  const result: string[] = [];
  for (let i = 0; i < 26; i++) {
    while (last[i] > 0) {
      result.push(String.fromCharCode(i + "a".charCodeAt(0)));
      last[i]--;
    }
  }

  return result;
}

function count(word: string): number[] {
  const frequency = Array(26).fill(0);
  for (let char of word) {
    frequency[char.charCodeAt(0) - "a".charCodeAt(0)]++;
  }
  return frequency;
}

function intersection(freq1: number[], freq2: number[]) {
  return freq1.map((f1, idx) => Math.min(f1, freq2[idx]));
}
