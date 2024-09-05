#!/usr/bin/node

// Print the list of characters in a Star Wars movie.

const request = require('request');

/**
 * Retrieves information about a Star Wars movie from the SWAPI API and prints
 * the names of all characters in the movie.
 *
 * @param {string} movieId - The ID of the movie to fetch.
 * @returns {void}
 */

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

/**
 * Makes a request to the SWAPI API to fetch movie details and character names.
 *
 * @callback requestCallback
 * @param {Error|null} error - The error object, if an error occurred.
 * @param {Object} response - The HTTP response object.
 * @param {string} body - The body of the response, containing the movie data.
 */

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  /**
   * The movie object parsed from the response body.
   * @type {Object}
   * @property {Array<string>} characters - URLs of the characters in the movie.
   */
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  /**
   * Fetches a character's name from the given URL.
   *
   * @param {string} url - The URL of the character resource.
   * @returns {Promise<string>} - A promise that resolves to the character's name.
   */
  const fetchCharacter = (url) => new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else if (response.statusCode !== 200) reject(new Error(`Invalid status code: ${response.statusCode}`));
      else resolve(JSON.parse(body).name);
    });
  });

  // Fetches all characters concurrently and prints their names
  Promise.all(characterUrls.map(fetchCharacter))
    .then((characters) => {
      characters.forEach((character) => console.log(character));
    })
    .catch((error) => console.error('Error:', error));
});
