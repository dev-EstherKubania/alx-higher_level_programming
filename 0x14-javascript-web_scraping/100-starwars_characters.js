#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // Loop through each character and fetch their information
    characters.forEach(characterUrl => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error(characterError);
        } else {
          const character = JSON.parse(characterBody);
          console.log(character.name);
        }
      });
    });
  }
});
