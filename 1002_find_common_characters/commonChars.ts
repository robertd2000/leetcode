function commonChars(words: string[]): string[] {
  if (words.length === 1) {
    return words[0].split("");
  }

  const res: string[] = [];
  const chars = new Set(words[0]);

  chars.forEach((char) => {
    let freq = Infinity;

    words.forEach((word) => {
      let count = word.split("").filter((c) => c === char).length;
      freq = Math.min(freq, count);
    });

    for (let i = 0; i < freq; i++) {
      res.push(char);
    }
  });

  return res;
}
