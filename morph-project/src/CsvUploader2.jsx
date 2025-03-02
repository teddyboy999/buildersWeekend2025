import { useState } from 'react';
import Papa from 'papaparse';
import { supabase } from './supabaseClient';

const CsvUploader2 = ({ onDataLoaded }) => {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState('');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) {
      setStatus('No file selected');
      return;
    }

    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: async (result) => {
        const expectedColumns = ['product_id', ...Array.from({ length: 30 }, (_, i) => `day${i + 1}`)];
        if (!expectedColumns.every(col => col in result.data[0])) {
          setStatus('CSV must have product_id, day1, ..., day30');
          return;
        }

        const formattedData = result.data.map(row => ({
          product_id: row.product_id,
          ...Object.fromEntries(
            Array.from({ length: 30 }, (_, i) => [`day${i + 1}`, parseInt(row[`day${i + 1}`]) || 0])
          ),
        }));

        setData(formattedData);
        setStatus('File loaded — uploading to Supabase...');

        try {
          const { error } = await supabase
            .from('stock_data3')
            .insert(formattedData);

          if (error) throw error;
          setStatus('File uploaded to Supabase');
          onDataLoaded(formattedData);
        } catch (error) {
          setStatus(`Error uploading: ${error.message}`);
          console.error('Upload error:', error);
        }
      },
      error: (error) => {
        setStatus(`Parse error: ${error.message}`);
      },
    });
  };

  return (
    <div className="p-4 border rounded-lg shadow-md w-full max-w-4xl mx-auto">
      <input
        type="file"
        accept=".csv"
        onChange={handleFileUpload}
        className="mb-4"
      />
      {status && <p className="mb-4">{status}</p>}
      {data.length > 0 && (
        <div
          className="resizable-container border border-gray-400 rounded"
          style={{
            width: '100%', // Initial width
            minWidth: '300px', // Minimum width to prevent collapse
            height: '400px', // Initial height
            minHeight: '200px', // Minimum height
            overflow: 'auto', // Required for resize to work
            resize: 'both', // Allows resizing in both directions
          }}
        >
          <table className="border-collapse border border-gray-400 w-full">
            <thead>
              <tr>
                {Object.keys(data[0]).map((key) => (
                  <th key={key} className="border border-gray-300 p-2 bg-gray-100">
                    {key}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, index) => (
                <tr key={index}>
                  {Object.values(row).map((value, idx) => (
                    <td key={idx} className="border border-gray-300 p-2">
                      {value}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default CsvUploader2;