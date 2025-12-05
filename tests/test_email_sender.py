import os
from unittest.mock import patch, MagicMock
from src import email_sender

def test_send_report_with_mock():
    """Test send_report with mocked SMTP to avoid actual email sending."""
    mock_pdf_path = "reports/test_report.pdf"
    
    # Mock the file open to simulate PDF file
    mock_file_content = b"mock pdf content"
    
    with patch("builtins.open", create=True) as mock_open:
        mock_file = MagicMock()
        mock_file.read.return_value = mock_file_content
        mock_open.return_value.__enter__.return_value = mock_file
        
        with patch("smtplib.SMTP_SSL") as mock_smtp:
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            with patch.dict(os.environ, {
                "EMAIL_USER": "test@gmail.com",
                "EMAIL_PASS": "test_password"
            }):
                email_sender.send_report(mock_pdf_path)
                
                # Verify SMTP login was called
                mock_smtp_instance.login.assert_called_once_with("test@gmail.com", "test_password")
                
                # Verify send_message was called
                mock_smtp_instance.send_message.assert_called_once()
