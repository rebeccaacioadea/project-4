
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Bulma from 'bulma'
// import SearchBar from './SearchBar'


const Books = (props) => {

  const [books, updateBooks] = useState([])
  const [words, updateWords] = useState('')
  const [bookData, updateBookData] = useState([])
  const [title, updateTitle] = useState('')

  useEffect(() => {
    axios.get('/api/books')
      .then((resp) => {
        updateBooks(resp.data)
        console.log(resp.data)
      })
  }, [])

  console.log(books)

  return <div className="section">

    {/* <h2> Books Page</h2> */}
    <div className="columns is-multiline is-mobile">
      {books.map((book, index) => {
        return <div className="column is-one-third-desktop is-half-tablet is-half-mobile"
          key={index}>
          <Link to={{ pathname: `/books/${book.id}`, state: { book } }} >
            <section class="cards">
              <article class="card card--2">
                {/* <div class="card__info-hover"> */}
                {/* </div>  */}
                {/* <div class="card__img"></div> */}
                <a href="#" class="card_link">
                  <img src={book.image} alt={book.title} />
                  <div class="card__img--hover"></div>
                </a>
                <div class="card__info">
                  <h1 class="card__title">{book.title}</h1>
                  <span class="card__by">by <a href="#" class="card__author" title="author">{book.author}</a></span>

                </div>
              </article>
            </section>
            {/* <div className="card">
        <div className="card-content">
          <div className="media">
            <div className="media-content">
              <h2 className="title is-4">
                {book.title}
              </h2>
              <p className="subtitle is-4">
                {book.author}
              </p>
            </div>
          </div>
        </div>
        <div className="card-image">
          <figure className="image is-4by3">
            <img src={book.image} alt={book.title} />
          </figure>
        </div>
      </div>  */}
          </Link>
        </div>
      })}
    </div>
  </div>
}

export default Books
