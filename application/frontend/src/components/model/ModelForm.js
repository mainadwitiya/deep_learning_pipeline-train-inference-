import { useHistory, useLocation } from "react-router";

const ModelForm = (props) => {
  // const [fileTitle, setFileTitle] = useState("");
  // const [fileDesc, setFileDesc] = useState("");
  // const [file, setFile] = useState("");
  // const [fileData, setFileData] = useState({
  //   // title: "",
  //   // content: "",
  //   training_data: "",
  //   validate_data: "",
  //   label_data: "",
  // });

  const history = useHistory();
  const location = useLocation();

  // console.log("history", history);
  // console.log("location", location);

  // const titleChangeHandler = (e) => {
  //   setFileData({ ...fileData, title: e.target.value });
  // };

  // const descChangeHandler = (e) => {
  //   setFileData({ ...fileData, content: e.target.value });
  // };

  const formSubmitHandler = async (e) => {
    e.preventDefault();
    // let form_data = new FormData();
    // form_data.append("file_data", fileData.files);
    // form_data.append("title", fileData.title);
    // form_data.append("content", fileData.content);
    // let url = "http://127.0.0.1:8000/apis/model_records/";
    // axios
    //   .post(url, form_data, {
    //     headers: {
    //       "content-type": "multipart/form-data",
    //     },
    //   })
    //   .then((res) => {
    //     console.log(res.data);
    //   })
    //   .catch((err) => console.log(err));

    history.push(location.pathname + "/select-arch");
  };
  // console.log(fileData);
  return (
    <form onSubmit={formSubmitHandler}>
      {/* <div className="form-group">
        <label htmlFor="title">File Name</label>
        <input
          className="form-control"
          type="text"
          name="title"
          id="title"
          placeholder="ex. Record One"
          onChange={titleChangeHandler}
          value={fileData.title}
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
          value={fileData.content}
        />
      </div> */}
      <div className="form-group my-4">
        <label htmlFor="training_file">
          <strong>Upload Training Data File</strong>
        </label>
        <input
          type="file"
          className="form-control-file"
          accept="file_extension/ .tfrecords ,file_extension/ .record ,file_extension/ .tfrecord, file_extension/ .records"
          id="training_file"
          onChange={props.onUploadTrainingFile}
          required
        />
      </div>
      <div className="form-group my-4">
        <label htmlFor="validation_file">
          <strong>Upload Validation File</strong>
        </label>
        <input
          type="file"
          className="form-control-file"
          accept="file_extension/ .tfrecords ,file_extension/ .record ,file_extension/ .tfrecord, file_extension/ .records"
          id="validation_file"
          onChange={props.onUploadValidationFile}
          required
        />
      </div>
      <div className="form-group my-4">
        <label htmlFor="label_file">
          <strong>Upload Label File</strong>
        </label>
        <input
          type="file"
          className="form-control-file"
          accept="file_extension/ .pbtxt"
          id="label_file"
          onChange={props.onUploadLabelFile}
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
