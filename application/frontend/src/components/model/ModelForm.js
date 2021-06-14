import { useHistory, useLocation } from "react-router";

const ModelForm = (props) => {
  const history = useHistory();
  const location = useLocation();

  const formSubmitHandler = async (e) => {
    e.preventDefault();
    history.push(location.pathname + "/select-arch");
  };
  return (
    <form onSubmit={formSubmitHandler}>
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
