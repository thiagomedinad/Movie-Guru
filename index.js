const express = require('express');
const cors = require('cors');
const fs = require('fs');
const papa = require('papaparse');

const app = express();
app.use(cors());

const CSV_FILE_PATH = 'imdb_top_1000.csv';

app.get('/random-movies', (req, res) => {
  const file = fs.createReadStream(CSV_FILE_PATH);
  papa.parse(file, {
    header: true,
    complete: (results) => {
      let movies = results.data;
      movies = movies.map((movie) => {
        for (let key in movie) {
          if (movie[key] === '' || movie[key] === 'N/A') {
            movie[key] = null;
          }
        }
        return movie;
      });
      const randomMovies = [];
      for (let i = 0; i < 5; i++) {
        const randomIndex = Math.floor(Math.random() * movies.length);
        randomMovies.push(movies[randomIndex]);
      }
      res.json(randomMovies);
    },
    error: (error) => {
      console.error(error);
      res.status(500).send('An error occurred while parsing the CSV file.');
    }
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
