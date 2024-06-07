function replaceWords(dictionary: string[], sentence: string): string {
  const map = {};
  const res: string[] = [];

  for (let i of sentence.split(" ")) {
    const word = dictionary
      .filter((d) => i.startsWith(d))
      ?.sort((a, b) => a.length - b.length)?.[0];

    if (word) {
      map[i] = word;
    }

    if (map[i]) {
      res.push(map[i]);
    } else {
      res.push(i);
    }
  }

  return res.join(" ");
}
