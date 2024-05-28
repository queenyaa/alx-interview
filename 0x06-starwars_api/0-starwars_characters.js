#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  const printCharacterNames = (urls, index) => {
    if (index >= urls.length) {
      return;
    }

    request(urls[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacterNames(urls, index + 1);
    });
  };

  printCharacterNames(characterUrls, 0);
});
