// DeleteDocumentComponent.js

import React from 'react';

const DeleteDocumentComponent = ({ documentId, onDelete }) => {
  // تابع برای حذف مستند
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this document?')) {
      onDelete(documentId); // فراخوانی تابع onDelete برای حذف مستند
    }
  };

  return (
    <button
      onClick={handleDelete}
      style={{
        backgroundColor: '#dc3545',
        color: 'white',
        padding: '10px 15px',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
      }}
    >
      Delete Document
    </button>
  );
};

export default DeleteDocumentComponent;