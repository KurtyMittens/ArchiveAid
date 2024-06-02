#!/usr/bin/bash

echo "Archive/Aid Archlinux installer: Do you want to proceed? (yes/no):"
read RESPONSE

if [ ${RESPONSE,,} = yes ]; then
   cp ArchiveAid.desktop ~/.local/share/applications/
   echo DONE: .desktop is created to .local/share/applications
else
   echo "Okiee Bye!"
fi 