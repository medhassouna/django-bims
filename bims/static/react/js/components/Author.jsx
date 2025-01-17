import React from 'react';
import update from 'immutability-helper';
import Autosuggest from 'react-autosuggest';
import axios from 'axios';

// Use your imagination to render suggestions.
const renderSuggestion = (suggestion, index) => (
  <div data-author-index={index} data-author-id={suggestion.id}>
    {suggestion.first_name} {suggestion.last_name}
  </div>
);


class Author extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      value: '',
      authors: [],
      suggestions: [],
      mounted: false
    }

    this.mounted = false;
    this.handleChange = this.handleChange.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.addNewAuthor = this.addNewAuthor.bind(this);
  }

  updateAuthors() {
    const authors = [];
    for (let i = 0; i < this.props.authors.length; i++) {
      const author = this.props.authors[i];
      author.full_name = `${author.first_name} ${author.last_name}`
      authors.push(author)
    }
    if (authors.length === 0) {
      authors.push('')
    }
    this.setState({
      authors: authors
    })
  }

  addNewAuthor(e) {
    e.preventDefault();
    this.setState(update(this.state, {
      authors: {$push: ['']}
    }))
  }

  componentDidMount() {
    this.setState({
      mounted: true
    })
    this.updateAuthors();
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    if (!this.state.mounted) {
      return false;
    }
    if (JSON.stringify(prevProps.authors) !== JSON.stringify(this.props.authors)) {
      this.updateAuthors();
    }
  }

  handleClick(event) {
    event.target.select();
  }

  handleChange(event, { newValue }) {
    let authorIndex = event.nativeEvent.target.dataset.authorIndex;
    let authorId = null;
    if (typeof authorIndex === 'undefined') {
      authorIndex = $(event.nativeEvent.target).data('author-index');
      authorId = $(event.nativeEvent.target).data('author-id');
    }
    this.setState(update(this.state, {
      authors: {
        [authorIndex]: { $set: newValue }
      }
    }))
  }

  onSuggestionsFetchRequested = ({value}) => {
    axios.get('/user-autocomplete/?term=' + encodeURIComponent(value)
    ).then((response) => {
        if (response.data !== 'fail') {
          this.setState({
            suggestions: response.data
          })
        }}
    ).catch(error => console.error(error))
  }

  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  }

  // When suggestion is clicked, Autosuggest needs to populate the input
  // based on the clicked suggestion. Teach Autosuggest how to calculate the
  // input value for every given suggestion.
  getSuggestionValue = (suggestion, index) => {
    return suggestion;
  }

  render() {

    const {suggestions} = this.state

    return (
      <div className="form-group">
        <label>Author(s)</label>
        {this.state.authors.map((author, index) =>
          {
            const value = author.first_name ? author.first_name + ' ' + author.last_name : author;
            const renderInputComponent = inputProps => {
              delete inputProps.className;
              return (
                  <div>
                      <input
                          onClick={this.handleClick}
                          data-author-index={index} data-author-id={author.id} className={"form-control"}  {...inputProps}/>
                  </div>
              );
            }
             const inputProps = {
              placeholder: (
                  "Author's name with following format: [First name] [Space] [Last name]"
              ),
              value,
              onChange: this.handleChange
            };
            return <div style={{ marginTop: 10 }}><Autosuggest
              suggestions={suggestions}
              onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
              onSuggestionsClearRequested={this.onSuggestionsClearRequested}
              getSuggestionValue={(suggestion) => this.getSuggestionValue(suggestion, index)}
              renderSuggestion={(suggestion) => renderSuggestion(suggestion, index)}
              renderInputComponent={renderInputComponent}
              inputProps={inputProps}
            /></div>
          }
        )}
        <br/>
        <button className="btn btn-default" onClick={this.addNewAuthor}>Add new author
        </button>
      </div>

    )
  }
}

export default Author
