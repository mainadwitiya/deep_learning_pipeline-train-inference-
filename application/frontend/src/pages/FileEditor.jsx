import React from "react";
import { ContentState, Editor, EditorState } from "draft-js";

import FileContext from "../components/utils/FileContext";
import classes from "./FileEditor.module.css";

// import data from "./Data.json";

const FileEditor = () => {
  const fileContext = React.useContext(FileContext);

  const content = ContentState.createFromText(fileContext.fileData);

  const [editorState, setEditorState] = React.useState(
    EditorState.createWithContent(content)
  );

  const onChangeEditorHandler = (editorState) => {
    setEditorState(editorState);
  };

  return (
    <div className={classes.mainRoot}>
      <div className={classes.editor}>
        <Editor editorState={editorState} onChange={onChangeEditorHandler} />
      </div>
    </div>
  );
};

export default FileEditor;
