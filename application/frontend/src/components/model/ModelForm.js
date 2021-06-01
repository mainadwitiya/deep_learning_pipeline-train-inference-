import axios from "axios";
import { useState } from "react";
import { useHistory } from "react-router";

const ModelForm = () => {
  const [fileTitle, setFileTitle] = useState("");
  const [fileDesc, setFileDesc] = useState("");
  const [file, setFile] = useState("");
  const API = "http://127.0.0.1:8000/apis";

  const history = useHistory();

  const titleChangeHandler = (e) => {
    setFileTitle(e.target.value);
  };

  const descChangeHandler = (e) => {
    setFileDesc(e.target.value);
  };

  const fileUploadHandler = (e) => {
    setFile(e.target.files[0]);
  };

  const formSubmitHandler = (e) => {
    e.preventDefault();

    const formData = {
      title: fileTitle,
      content: fileDesc,
      file: file,
    };

    // Handles request
    axios({
      method: "POST",
      url: `${API}/model_records`,
      data: JSON.stringify(formData),
      headers: {
        "Content-Type": "application/json",
      },
    }).then((response) => {
      console.log(response.data);
    });

    // Redirect to page
    history.push("/model/select-arch");
  };

  return (
    <form onSubmit={formSubmitHandler}>
      <div className="form-group">
        <label htmlFor="title">File Name</label>
        <input
          className="form-control"
          type="text"
          name="title"
          id="title"
          placeholder="ex. Record One"
          onChange={titleChangeHandler}
          value={fileTitle}
        />
      </div>
      <div className="form-group">
        <label htmlFor="desc">File Description</label>
        <input
          className="form-control"
          type="text"
          name="desc"
          id="desc"
          placeholder="ex. Data to train model."
          onChange={descChangeHandler}
          value={fileDesc}
        />
      </div>
      <div className="form-group">
        <label htmlFor="desc">Upload File</label>
        <input
          type="file"
          className="form-control-file"
          accept="file_extension/ .tfrecords ,file_extension/ .record ,file_extension/ .tfrecord, file_extension/ .records"
          id="file"
          onChange={fileUploadHandler}
          required
        />
      </div>

      <div className="text-center">
        <button className="btn btn-primary px-4" type="submit">
          Upload
        </button>
      </div>
    </form>
  );
};

export default ModelForm;
