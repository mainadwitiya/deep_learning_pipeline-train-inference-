import React, { Component } from "react";
import axios from "axios";

class ModelPage extends Component {
  state = {
    title: "",
    content: "",
    file_data: null,
  };

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value,
    });
  };

  handleImageChange = (e) => {
    this.setState({
      file_data: e.target.files[0],
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append(
      "file_data",
      this.state.file_data,
      this.state.file_data.name
    );
    form_data.append("title", this.state.title);
    form_data.append("content", this.state.content);
    let url = "http://127.0.0.1:8000/apis/model_records/";
    axios
      .post(url, form_data, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <p>
            <input
              type="text"
              placeholder="File Name"
              id="title"
              value={this.state.title}
              onChange={this.handleChange}
              required
            />
          </p>
          <p>
            <input
              type="text"
              placeholder="Description"
              id="content"
              value={this.state.content}
              onChange={this.handleChange}
              required
            />
          </p>
          <p>
            <input
              type="file"
              id="image"
              accept="file_extension/ .tfrecords ,file_extension/ .record ,file_extension/ .tfrecord, file_extension/ .records"
              onChange={this.handleImageChange}
              required
            />
          </p>
          <input type="submit" />
        </form>
      </div>
    );
  }
}

export default ModelPage;
