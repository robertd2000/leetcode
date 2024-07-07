declare global {
  interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>;
  }
}

Array.prototype.groupBy = function (fn) {
  return this.reduce((group, item) => {
    let key = fn(item);

    if (group[key]) {
      group[key].push(item);
    } else {
      group[key] = [item];
    }

    return group;
  }, {});
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
