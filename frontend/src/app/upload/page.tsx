'use client';

import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, FileText, CheckCircle, AlertCircle, Loader2, X, Eye, Trash2 } from 'lucide-react';

interface UploadedTable {
  table_name: string;
  display_name: string;
  row_count: number;
  created_at: string;
  file_name: string;
  columns: string[];
}

interface UploadResponse {
  success: boolean;
  message?: string;
  error?: string;
  data?: {
    table_name: string;
    rows_inserted: number;
    columns_created: number;
    file_size: number;
    validation: any;
    metadata: any;
  };
}

export default function UploadPage() {
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploadResult, setUploadResult] = useState<UploadResponse | null>(null);
  const [uploadedTables, setUploadedTables] = useState<UploadedTable[]>([]);
  const [showPreview, setShowPreview] = useState(false);
  const [previewData, setPreviewData] = useState<any[]>([]);
  const [tableName, setTableName] = useState('');

  // Mock client ID for demo
  const CLIENT_ID = '550e8400-e29b-41d4-a716-446655440000';

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (file && file.type === 'text/csv' || file.name.endsWith('.csv')) {
      setUploadedFile(file);
      setUploadResult(null);
      setTableName(file.name.replace('.csv', ''));
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv']
    },
    multiple: false
  });

  const handleUpload = async () => {
    if (!uploadedFile) return;

    setIsUploading(true);
    setUploadProgress(0);

    const formData = new FormData();
    formData.append('csv_file', uploadedFile);
    formData.append('client_id', CLIENT_ID);
    formData.append('table_name', tableName);

    try {
      // Simulate progress
      const progressInterval = setInterval(() => {
        setUploadProgress(prev => {
          if (prev >= 90) {
            clearInterval(progressInterval);
            return 90;
          }
          return prev + 10;
        });
      }, 200);

      const response = await fetch('/api/upload-csv', {
        method: 'POST',
        body: formData,
      });

      clearInterval(progressInterval);
      setUploadProgress(100);

      const result: UploadResponse = await response.json();
      setUploadResult(result);

      if (result.success) {
        // Refresh uploaded tables list
        fetchUploadedTables();
      }

    } catch (error) {
      setUploadResult({
        success: false,
        error: 'Upload failed. Please try again.'
      });
    } finally {
      setIsUploading(false);
      setUploadProgress(0);
    }
  };

  const fetchUploadedTables = async () => {
    try {
      const response = await fetch(`/api/uploaded-tables?client_id=${CLIENT_ID}`);
      const data = await response.json();
      if (data.success) {
        setUploadedTables(data.tables);
      }
    } catch (error) {
      console.error('Failed to fetch uploaded tables:', error);
    }
  };

  const handleDeleteTable = async (tableName: string) => {
    try {
      const response = await fetch('/api/delete-table', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          client_id: CLIENT_ID,
          table_name: tableName
        }),
      });

      const result = await response.json();
      if (result.success) {
        fetchUploadedTables();
      }
    } catch (error) {
      console.error('Failed to delete table:', error);
    }
  };

  const handlePreviewTable = async (tableName: string) => {
    try {
      const response = await fetch(`/api/table-data?client_id=${CLIENT_ID}&table_name=${tableName}&limit=10`);
      const data = await response.json();
      if (data.success) {
        setPreviewData(data.data);
        setShowPreview(true);
      }
    } catch (error) {
      console.error('Failed to preview table:', error);
    }
  };

  React.useEffect(() => {
    fetchUploadedTables();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-slate-800 mb-2">CSV Upload System</h1>
          <p className="text-slate-600">Upload your CSV files and automatically create dynamic database tables</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Upload Section */}
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
              <h2 className="text-xl font-semibold text-slate-800 mb-4">Upload CSV File</h2>
              
              {/* Drag & Drop Zone */}
              <div
                {...getRootProps()}
                className={`border-2 border-dashed rounded-lg p-8 text-center transition-all duration-200 cursor-pointer ${
                  isDragActive
                    ? 'border-blue-400 bg-blue-50'
                    : 'border-slate-300 hover:border-slate-400 hover:bg-slate-50'
                }`}
              >
                <input {...getInputProps()} />
                <Upload className="mx-auto h-12 w-12 text-slate-400 mb-4" />
                {isDragActive ? (
                  <p className="text-blue-600 font-medium">Drop the CSV file here...</p>
                ) : (
                  <div>
                    <p className="text-slate-600 mb-2">
                      Drag & drop a CSV file here, or click to select
                    </p>
                    <p className="text-sm text-slate-500">Maximum file size: 10MB</p>
                  </div>
                )}
              </div>

              {/* File Preview */}
              {uploadedFile && (
                <div className="mt-4 p-4 bg-slate-50 rounded-lg">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <FileText className="h-5 w-5 text-slate-600" />
                      <div>
                        <p className="font-medium text-slate-800">{uploadedFile.name}</p>
                        <p className="text-sm text-slate-500">
                          {(uploadedFile.size / 1024 / 1024).toFixed(2)} MB
                        </p>
                      </div>
                    </div>
                    <button
                      onClick={() => setUploadedFile(null)}
                      className="text-slate-400 hover:text-slate-600"
                    >
                      <X className="h-5 w-5" />
                    </button>
                  </div>
                </div>
              )}

              {/* Table Name Input */}
              {uploadedFile && (
                <div className="mt-4">
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Table Name
                  </label>
                  <input
                    type="text"
                    value={tableName}
                    onChange={(e) => setTableName(e.target.value)}
                    className="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Enter table name..."
                  />
                </div>
              )}

              {/* Upload Button */}
              {uploadedFile && (
                <button
                  onClick={handleUpload}
                  disabled={isUploading || !tableName}
                  className="w-full mt-4 bg-blue-600 text-white py-3 px-4 rounded-lg font-medium hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  {isUploading ? (
                    <div className="flex items-center justify-center space-x-2">
                      <Loader2 className="h-5 w-5 animate-spin" />
                      <span>Uploading...</span>
                    </div>
                  ) : (
                    'Upload CSV'
                  )}
                </button>
              )}

              {/* Progress Bar */}
              {isUploading && (
                <div className="mt-4">
                  <div className="w-full bg-slate-200 rounded-full h-2">
                    <div
                      className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${uploadProgress}%` }}
                    />
                  </div>
                  <p className="text-sm text-slate-600 mt-2 text-center">
                    Processing CSV file... {uploadProgress}%
                  </p>
                </div>
              )}

              {/* Upload Result */}
              {uploadResult && (
                <div className={`mt-4 p-4 rounded-lg ${
                  uploadResult.success
                    ? 'bg-green-50 border border-green-200'
                    : 'bg-red-50 border border-red-200'
                }`}>
                  <div className="flex items-center space-x-2">
                    {uploadResult.success ? (
                      <CheckCircle className="h-5 w-5 text-green-600" />
                    ) : (
                      <AlertCircle className="h-5 w-5 text-red-600" />
                    )}
                    <span className={`font-medium ${
                      uploadResult.success ? 'text-green-800' : 'text-red-800'
                    }`}>
                      {uploadResult.success ? 'Upload Successful!' : 'Upload Failed'}
                    </span>
                  </div>
                  <p className={`text-sm mt-1 ${
                    uploadResult.success ? 'text-green-700' : 'text-red-700'
                  }`}>
                    {uploadResult.message || uploadResult.error}
                  </p>
                  {uploadResult.success && uploadResult.data && (
                    <div className="mt-3 text-sm text-green-700">
                      <p>• {uploadResult.data.rows_inserted} rows inserted</p>
                      <p>• {uploadResult.data.columns_created} columns created</p>
                      <p>• Table: {uploadResult.data.table_name}</p>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>

          {/* Uploaded Tables Section */}
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
              <h2 className="text-xl font-semibold text-slate-800 mb-4">Uploaded Tables</h2>
              
              {uploadedTables.length === 0 ? (
                <div className="text-center py-8 text-slate-500">
                  <FileText className="mx-auto h-12 w-12 text-slate-300 mb-4" />
                  <p>No uploaded tables yet</p>
                  <p className="text-sm">Upload a CSV file to get started</p>
                </div>
              ) : (
                <div className="space-y-3">
                  {uploadedTables.map((table) => (
                    <div
                      key={table.table_name}
                      className="p-4 border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors"
                    >
                      <div className="flex items-center justify-between">
                        <div className="flex-1">
                          <h3 className="font-medium text-slate-800">{table.display_name}</h3>
                          <p className="text-sm text-slate-500">{table.file_name}</p>
                          <div className="flex items-center space-x-4 mt-2 text-xs text-slate-600">
                            <span>{table.row_count} rows</span>
                            <span>{table.columns.length} columns</span>
                            <span>{new Date(table.created_at).toLocaleDateString()}</span>
                          </div>
                        </div>
                        <div className="flex items-center space-x-2">
                          <button
                            onClick={() => handlePreviewTable(table.table_name)}
                            className="p-2 text-slate-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                            title="Preview data"
                          >
                            <Eye className="h-4 w-4" />
                          </button>
                          <button
                            onClick={() => handleDeleteTable(table.table_name)}
                            className="p-2 text-slate-600 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                            title="Delete table"
                          >
                            <Trash2 className="h-4 w-4" />
                          </button>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Data Preview Modal */}
        {showPreview && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-xl shadow-xl max-w-4xl w-full max-h-[80vh] overflow-hidden">
              <div className="flex items-center justify-between p-6 border-b border-slate-200">
                <h3 className="text-lg font-semibold text-slate-800">Data Preview</h3>
                <button
                  onClick={() => setShowPreview(false)}
                  className="text-slate-400 hover:text-slate-600"
                >
                  <X className="h-6 w-6" />
                </button>
              </div>
              <div className="p-6 overflow-auto max-h-[60vh]">
                {previewData.length > 0 ? (
                  <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                      <thead>
                        <tr className="border-b border-slate-200">
                          {Object.keys(previewData[0]).map((key) => (
                            <th key={key} className="text-left py-2 px-3 font-medium text-slate-700">
                              {key}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {previewData.map((row, index) => (
                          <tr key={index} className="border-b border-slate-100">
                            {Object.values(row).map((value, cellIndex) => (
                              <td key={cellIndex} className="py-2 px-3 text-slate-600">
                                {String(value)}
                              </td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                ) : (
                  <p className="text-slate-500 text-center py-8">No data available</p>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
} 